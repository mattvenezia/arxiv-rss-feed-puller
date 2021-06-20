import feedparser

rssfeed = feedparser.parse("http://arxiv.org/rss/cs.CR")
num_entries = len(rssfeed.entries)
print("====================")
print(rssfeed.feed.title)
print("====================")
print('NUM ENTRIES: '+str(num_entries))
print("====================")

for i in range(num_entries):
	entry = rssfeed.entries[i]
	print("**************************************")
	print("PAPER NO: "+str(i+1))
	print('ID: '+entry.id)
	print('TITLE: '+entry.title)
	print('SUMMARY: '+entry.summary)
	print("**************************************")



