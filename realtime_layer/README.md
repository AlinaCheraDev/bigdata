-Start Docker Desktop

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
