FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.1
MAINTAINER luk <kuczynskilukasz@gmail.com>

RUN elasticsearch-plugin install analysis-stempel
RUN sysctl -w vm.max_map_count=262144


