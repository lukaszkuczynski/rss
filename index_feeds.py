from elasticsearch import Elasticsearch
from elasticsearch import helpers
from csv import DictReader

es = Elasticsearch()


path = "./logstash/cssed_feeds/full_feed.csv"
def gen_bulk_actions():
    with open(path) as f:
        reader = DictReader(f, fieldnames=['title','link','created_at','text'])
        for elem in reader:
            yield {
                "_action": "insert",
                "_index": "infopraca_rss",
                "_type": "offer",
                "_source": dict(elem)
            }


helpers.bulk(es, actions=gen_bulk_actions())