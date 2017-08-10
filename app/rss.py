import feedparser
import json
import os
from csv import DictWriter

url = 'http://infopraca.pl/rss'





file_feed_simple = 'data/simple_feed.csv'
file_feed_full = 'data/full_feed.csv'
file_last_entries = 'data/last.json'
file_last_rss_update = 'data/updated'


def check_if_rss_update_changed(update_from_feed):
    if not os.path.isfile(file_last_rss_update):
        with open(file_last_rss_update, 'w') as f:
            f.write('')
    with open(file_last_rss_update) as f:
        content = f.read()
    if content != update_from_feed:
        return True
    else:
        return False

def prepare_entry_before_writing_to_csv(entry):
    if 'description' in entry:
        entry['description'] = entry['description'].replace("\n", " ")
    return entry

def append_entry_to_csv(entry):
    prepare_entry_before_writing_to_csv(entry)
    fieldnames_simple = ['title', 'link', 'published']
    fieldnames_full = ['title', 'link', 'published', 'description']
    with open(file_feed_simple, 'a', newline='', encoding='utf8') as f:
        writer = DictWriter(f, fieldnames_simple, extrasaction='ignore')
        writer.writerow(entry)
    with open(file_feed_full, 'a', newline='', encoding='utf8') as f:
        writer = DictWriter(f, fieldnames_full, extrasaction='ignore')
        writer.writerow(entry)



def append_to_csv(new_entries, last_entries_ids):
    for entry in new_entries:
        if entry.id not in last_entries_ids:
            append_entry_to_csv(entry)


def save_last_update(updated):
    with open(file_last_rss_update, 'w') as f:
        f.write(updated)



def save_last_entries(entries):
    with open(file_last_entries, 'w', encoding='utf8') as f:
        last_entries_ids = ([entry.id for entry in entries])
        txt = json.dumps(last_entries_ids)
        f.write(txt)


def read_last_entries():
    if not os.path.isfile(file_last_entries):
        with open(file_last_entries, 'w') as f:
            f.write('{}')
    with open(file_last_entries, encoding='utf8') as f:
        try:
            last = json.load(f)
            return last
        except:
            return []


def main():
    d = feedparser.parse(url)
    rss_updated = d.feed.updated
    if check_if_rss_update_changed(rss_updated):
        print('changed update time %s' % d.feed.updated)
        last_entries = read_last_entries()
        append_to_csv(d.entries, last_entries)
        save_last_update(rss_updated)
        save_last_entries(d.entries)
    else:
        print('update time not changed')



if __name__ == '__main__':
    main()
