import csv
import time
import sys
#import json
#from kafka import KafkaProducer

def stream_csv_to_json(csv_path, delimiter=","):
  with open(csv_path, newline='') as f:
    reader = csv.DictReader(f, delimiter=delimiter)
    for row in reader:
        #print(row)
        yield row

def main():
  try:
    # assert len(sys.argv) > 1, "Please provide the path to the CSV file as an argument."
    # csv_file = sys.argv[1]

    # # Connect to Kafka broker (default localhost:9092)
    # producer = KafkaProducer(
    #     bootstrap_servers=['localhost:9092'],
    #     value_serializer=lambda v: json.dumps(v).encode('utf-8')
    # )
    
    for item in stream_csv_to_json('file.csv', delimiter=';'):
        time.sleep(1) #wait for 60 seconds to simulate streaming
        print(item)

        # # Send each row as JSON to topic 'simulator-data'
        # producer.send('energy-data', value=item)
        # print(f"Sent: {item}")
    
    # producer.flush()
    # producer.close()   
        
  except Exception as e:
    print(e)

if __name__ == "__main__":
  sys.exit(main())