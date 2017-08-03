# Rss Browser A.K.A. Czytajka
Based on Elasticsearch browser that will help me to 
 - find remote job 
 - play with ES queries
 
I want also to try Stempel, Polish extension for Elasticsearch.

# Usage
## Collect data
You can use Raspberry or other docker-ready machine to collect data.  This will require using image from `app` folder.

## Index your files
To index your files you can use prepared Logstash and Elasticsearch images in their respective folders.  First run Elasticsearch and install plugin. Then parse your downloaded files from machine.
