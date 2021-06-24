# arxiv-rss-feed-puller

### ABOUT
This script pulls recent Computer Science papers from arXiv in the cryptography / computer security category.
It works by first staging the titles of the most recent papers uploaded to arXiv in the last 24 hours. Then the program prompts the user for a title number to show show the abstract and link to the paper.

Currently, the crypto/security category is hardcoaded into the RSS link (...cs.CR) but you can change that. There is guidence here -> https://arxiv.org/help/rss.

You may be asking why I don't just use the arXiv API. Well, because you can't pull the new papers uploaded in the last 24 hours. I don't know why...but luckily that is exactly what the RSS /recent listing does. You can achieve this also through email but it sucks. 

### TODO
I believe the abstract request function will break on some inuputs. I am aware of inputting '0' returns the last index paper at the moment. Sorry.

I'd like to also give the user the option to re-print the title listing after they have viewed an abstract.
