#!/usr/bin/env python3
import feedparser

rssfeed = feedparser.parse("http://arxiv.org/rss/cs.CR")
num_entries = len(rssfeed.entries)
print("========================================")
print("FEED TITLE: "+rssfeed.feed.title)
print("========================================")
print('NUM ENTRIES: '+str(num_entries))
print("========================================")
print("TITLES:")
# Print titles
for i in range(num_entries):
	entry = rssfeed.entries[i]
	print('TITLE NO: '+str(i+1)+" - "+entry.title)
# Ask user for input number
while (1):
	num = input("Enter a TITLE NO ('q' for EXIT): ")
	if num =='q':
		break # quitting
	elif not num.isnumeric():
		print("thats not a number, jackass")
		print("try again homie")
	elif int(num) < 0 or int(num) > num_entries:
		print("not in correct range, jackass")
		print("try again")
	else:
		# prob good...hopefully
		entry = rssfeed.entries[int(num)-1]
		print("************************************************************************************************************")
		print("PAPER NO: "+str(num))
		print('ID: '+entry.id)
		print('TITLE: '+entry.title)
		print('SUMMARY: '+entry.summary)
		print("************************************************************************************************************")

print("EXITING...")
