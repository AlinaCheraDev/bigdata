from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_json, struct
from pyspark.sql.types import StructType, StructField, StringType

# Initialize Spark Session
spark = SparkSession.builder \
  .appName("EnergyDataStreaming") \
  .getOrCreate()

# Define schema for incoming JSON data
schema = StructType([
  StructField("Date", StringType(), True),
  StructField("Time", StringType(), True),
  StructField("Global_active_power", StringType(), True),
  StructField("Global_reactive_power", StringType(), True),
  StructField("Voltage", StringType(), True),
  StructField("Global_intensity", StringType(), True),
  StructField("Sub_metering_1", StringType(), True),
  StructField("Sub_metering_2", StringType(), True),
  StructField("Sub_metering_3", StringType(), True)
])

# Read from Kafka topic
df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("subscribe", "energy-data") \
  .option("startingOffsets", "latest") \
  .load()

# Parse JSON from Kafka value column
parsed_df = df.select(
  from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Convert to JSON for Kafka output
output_df = parsed_df.select(
    to_json(struct("*")).alias("value")
)

# Write to log file
query = output_df.writeStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("topic", "processed-data") \
  .option("checkpointLocation", "/opt/spark/app/checkpoint") \
  .start()

query.awaitTermination()