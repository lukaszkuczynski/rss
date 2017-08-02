input {
  file {
	path => "c:/p/logstash-5.5.1/bin/full_feed.csv"	
	start_position => beginning
    sincedb_path => "/dev/null"
    ignore_older => 0
  }
}

filter {
  csv {
	columns => ["title", "link", "created_at", "text"]
	}
	
   date {
match => ["created_at", "EEE, dd MMM YYYY HH:mm:ss Z"]
}
}

output {
  stdout { codec => json }
  elasticsearch {
	index => "infopraca"
	document_type => "offer"
  }
}