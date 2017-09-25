from crawler import Crawler
from consts import *

# create new instance of crawler and start crawling for the input url and search token
crawler = Crawler()

# Crawl for the first task
crawler.crawl(SEED_URL_FOR_TASK3)