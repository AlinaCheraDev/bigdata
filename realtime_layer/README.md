-Start Docker Desktop

-Open first PowerShell
PS C:\big_data> docker-compose build
PS C:\big_data> docker-compose up

-Open second PowerShell
PS C:\big_data> docker exec --workdir /opt/kafka/bin/ -it kafka sh
/opt/kafka/bin $ ./kafka-topics.sh --bootstrap-server kafka:9092 --list
/opt/kafka/bin $ ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic energy-data --from-beginning
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic processed-data --from-beginning

-go to first PowerShell
CTRL-C
PS C:\big_data> docker-compose down

docker compose down -v
docker compose up

docker build -t spark-streaming .
docker run --network realtime_layer_default spark-streaming
