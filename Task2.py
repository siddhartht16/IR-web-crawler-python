import sys
from crawler import Crawler

# read command line params
input_arguments = sys.argv[:]

seed_url = input_arguments[1]
search_token = input_arguments[2]

# create new instance of crawler and start crawling for the input url and search token
crawler = Crawler()

# Perform focused crawling
crawler.focused_crawl(seed_url, search_token)
