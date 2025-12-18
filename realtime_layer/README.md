HOW TO RUN

1. Start Docker Desktop
2. docker-compose build
3. docker-compose up
4. Verify that the data is inserted into Cassandra
   docker exec -it cassandra bash
   cqlsh
   DESCRIBE KEYSPACES;
   USE energy;
   DESCRIBE TABLES;
   select \* from events_by_hour;
5. Verify that the Kafa is working
   PS C:\big_data> docker exec --workdir /opt/kafka/bin/ -it kafka sh
   /opt/kafka/bin $ ./kafka-topics.sh --bootstrap-server kafka:9092 --list
   /opt/kafka/bin $ ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic raw-energy-data --from-beginning
   /opt/kafka/bin $ ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic processed-energy-data --from-beginning

IGNORE

-Open first PowerShell
PS C:\big_data> docker-compose build
PS C:\big_data> docker-compose up

docker compose up --build

-Open second PowerShell
PS C:\big_data> docker exec --workdir /opt/kafka/bin/ -it kafka sh
/opt/kafka/bin $ ./kafka-topics.sh --bootstrap-server kafka:9092 --list
/opt/kafka/bin $ ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic raw-energy-data --from-beginning
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic processed-energy-data --from-beginning

-go to first PowerShell
CTRL-C
PS C:\big_data> docker-compose down

docker compose down -v
docker compose up

docker build -t spark-streaming .
docker run --network realtime_layer_default spark-streaming

docker exec -it cassandra bash
cqlsh
DESCRIBE KEYSPACES;
USE energy;
DESCRIBE TABLES;
