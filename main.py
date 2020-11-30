import threading
from queue import Queue
from spider import spider
from domain import *
from general import *

PROJECT_NAME = 'sonder'
HOME_PAGE = 'https://sondernyonder.wordpress.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
# print(DOMAIN_NAME)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

# create worker threads (will die when main exists)


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
#
# do the next job in the queue


def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()
# each queued link is a new job


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()
#
# check if there are items in queue if so crawl


def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + ' links in the queue')
        create_jobs()


#
create_workers()
crawl()
