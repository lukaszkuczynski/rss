# Rss Browser A.K.A. Czytajka
Based on Elasticsearch browser that will help me to 
 - find remote job 
 - play with ES queries
 
I want also to try Stempel, Polish extension for Elasticsearch.

# Usage
## Collect
You can use Raspberry or other docker-ready machine to collect data.  This will require using image from `app` folder.
On your docker-ready machine just clone the repo and build the image using `build.sh` script.  Then run the existing image using
f.e. `run.sh` script, linking the volumes.  By default output CSV will be written to `/opt/rssparser/data` folder.
Each execution of script will make CSV bigger, filling it RSS feed entries.  As for the beginning the rss will be hardcoded to `infopraca.pl/rss` URL.
You can plan the execution of script periodically, f.e. putting `run.sh` as cron expression.


## Load
To index your files you can use prepared Logstash and Elasticsearch images in their respective folders. There is 
also python based loader made for this purpose.  First of all, download CSV file from the machine collecting data.
Then you can index files into elasticsearch.  Elastisearch comes with the prepared image, with polish Stempel included 
in it.  You can run the Elasticsearch+Kibana using `docker-compose.yml` script.
```bash
docker-compose up
```

## Search
Following there is a similar query you can run against the index after successful indexing:
```rest
POST infopraca_rss/offer/_search
{
	"query": {
		"bool": {
			"must": [
				{"match": {"text": "elasticsearch"}}
			],
			"should": [
				{"match": {"text": "java"}},
				{"match": {"text": "python"}}
			]
		}
	},
	"highlight": {
		"fields": {
			"text": {}
		}
	}
}
```
