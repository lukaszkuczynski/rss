/usr/share/logstash/bin/logstash -e 'input { stdin { } } output { stdout {} }'

# in case of problems with access to data folder
#  sudo chmod 777 /usr/share/logstash/data




