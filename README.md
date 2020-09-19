# Link_crawler (ongoing) 
bs_and_requests.py is a simple single spider, a basic crawler. It just displays the links and does not attempt to queue and crawl the links.
Rest of the files are the multi threaded spider crawler. When the main.py file is run it creates and stores links in two text files "queued.txt" and "crawled.txt". There seems to be a problem with the implementation of multi threading, the crawling freezes after some time, should investigate

