import feedparser

url = 'http://infopraca.pl/rss'
d = feedparser.parse(url)
print(d['feed'].keys())

file_out = 'data/out.csv'
file_last_entries = 'data/last.json'


for entry in d.entries:
    print(entry)




