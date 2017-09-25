# Constants required for crawler
# constant for max level
MAX_LEVEL_FOR_CRAWLING = 5

# constant for max parsed urls
LIMIT_FOR_MAX_CRAWLED_LINKS = 1000

# delay in seconds
DELAY_FOR_PARSING = 1

# constant for domain name url
WIKI_DOMAIN_NAME = "https://en.wikipedia.org"

# Constants for tasks
MODE_TASK1 = "TASK1"
MODE_TASK2 = "TASK2"
MODE_TASK3 = "TASK3"

# Constants for Task Files
TASK1_FILE_CONSTANT = "TASK1"
TASK2_A_FILE_CONSTANT = "TASK2-A"
TASK2_B_FILE_CONSTANT = "TASK2-B"
TASK3_FILE_CONSTANT = "TASK3"

# Extension for files
FILE_EXT = ".txt"

# file names for crawled files list and waiting files list
BFS_CRAWLED_PAGES_LIST = 'bfsCrawledPagesList'
BFS_QUEUED_PAGES_LIST = 'dfsQueuedPagesList'

DFS_CRAWLED_PAGES_LIST = 'dfsCrawledUrlsList'
DFS_QUEUED_PAGES_LIST = 'dfsQueuedUrlsList'

# keyword to be looked into
KEYWORD_FOR_FOCUSED_CRAWLING = "solar"

# Url constants for different tasks
SEED_URL_FOR_TASK1 = "https://en.wikipedia.org/wiki/Sustainable_energy"
SEED_URL_FOR_TASK3 = "https://en.wikipedia.org/wiki/Solar_power"

# Folder name for storing files
DIR_FOR_CRAWLER_FILES = 'crawlerfiles'

# Folder name for storing web pages data
DIR_FOR_DATA_FILES = 'datafiles'

# Constant for filename prefix
PREFIX_FOR_URL_DATA_FILE = "FileForUrlNo-"

# File name containing the url and data mapping
FILE_FOR_URL_DATA_MAPPING = "UrlDataFileMapping"