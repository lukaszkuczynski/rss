docker run -it --rm -v "$PWD":/conf -e ELASTICSEARCH_URL=http://localhost:9200 docker.elastic.co/logstash/logstash:5.5.0 logstash -f /conf/
