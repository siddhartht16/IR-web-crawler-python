from linkParser import LinkParserClass
from utils import *
from consts import *
from collections import deque
import time


# Main crawler Class
class Crawler:

    # private methods
    def __init__(self):
        """
        Constructor for Crawler
        """

        # initialize all variables for the crawler and set references
        # reference to hold seed url
        self.fseedurl = ''

        # reference for link parser instance
        self.flinkparser = None

        # list and counter to maintain the crawled sites list for bfs
        self.fcrawledsiteslist_bfs = deque()
        self.fcrawledsiteslistforprint_bfs = deque()
        self.fcrawledsitescount_bfs = 0

        #list and counter to maintian the crawled sites list for dfs
        self.fcrawledsiteslist_dfs = deque()
        self.fcrawledsiteslistforprint_dfs = deque()
        self.fcrawledsitescount_dfs = 0

        # list to maintain the queued files list
        #self.fqueuedsiteslist = deque()

        # queue for bfs crawling
        self.fqueueforbfs = deque()

        # stack for dfs crawling
        self.fstackfordfs = []

        # variable to keep track of current level
        self.fcurrentlevel = 0

        # variable for to save the text for focused crawling
        self.ffocusedcrawlkeyword = ''
        self.fisfocusedcrawl = False

        # variable to keep track of task
        self.fcurrenttask = ''

        # reference to hold file data mapping names
        self.ffilenamesmappinglist = []

        # reference to control data file writing of crawled urls
        self.fcanwriteurldatatofile = False

        # initialize and start
        self.initialize()

    def initialize(self):
        """
        Initialize directory and files for crawlers
        """
        # create folder for site
        # create_directory(DIR_FOR_CRAWLER_FILES)

        # create folder for storing crawled web pages
        # create_directory(DIR_FOR_DATA_FILES)

    def create_link_parser_class(self):
        # create link parser object if not already created
        if self.flinkparser is not None:
            self.flinkparser = None

        self.flinkparser = LinkParserClass(self)

    def crawl(self, p_seedurl):

        if not is_string_valid(p_seedurl):
            print "Please enter a valid seed url for crawling."
            return

        # set references for seed url and search token
        self.fseedurl = p_seedurl

        print "Initiating crawl for: "
        print "seed url: " + p_seedurl

        # Set the mode for the task
        if self.fseedurl == SEED_URL_FOR_TASK1:
            self.fcurrenttask = MODE_TASK1
        elif self.fseedurl == SEED_URL_FOR_TASK3:
            self.fcurrenttask = MODE_TASK3

        # create link parser
        self.create_link_parser_class()

        # Initiate breadth first crawling for the search token
        print "Initiating crawling for task: " + self.fcurrenttask
        self.crawl_bfs()
        print "Crawling complete"

    def focused_crawl(self, p_seedurl, p_searchtoken):

        if not is_string_valid(p_seedurl):
            print "Please enter a valid seed url for focused crawling."
            return

        if not is_string_valid(p_searchtoken):
            print "Please enter a valid search token for focused crawling."
            return

        # set references for seed url and search token as well as focused crawl mode
        self.fseedurl = p_seedurl
        self.ffocusedcrawlkeyword = p_searchtoken
        self.fisfocusedcrawl = True

        print "Initiating focused crawl for: "
        print "seed url: " + p_seedurl
        print "search token: " + p_searchtoken

        # Set the mode for the task
        self.fcurrenttask = MODE_TASK2

        # create link parser
        self.create_link_parser_class()

        # set the filter criteria with the link parser class
        self.flinkparser.set_filter_text(p_searchtoken)

        # Initiate breadth first crawling for the search token
        print "Initiating breadth first crawling"
        self.crawl_bfs()
        print "Breadth first crawling complete"

        print "Wait for 2 seconds..."

        # apply delay of 2 seconds
        time.sleep(2)

        # Initiate depth first crawling
        print "Initiating depth first crawling"
        self.crawl_dfs()
        print "Depth first crawling complete"

    def crawl_bfs(self):

        # parse for the seed
        lurlforparsing = self.fseedurl

        # set the current level
        self.fcurrentlevel = 1

        # remove contents from file mapping list
        del self.ffilenamesmappinglist[:]

        # get node for the seed url
        lnodeforurl = self.flinkparser.parse_using_bsoup(lurlforparsing, self.fcurrentlevel)

        if lnodeforurl is not None:

            # add node for seed url to bfs queue
            self.fqueueforbfs.append(lnodeforurl)

            # add seed url to crawled sites list
            if lurlforparsing not in self.fcrawledsiteslist_bfs:
                self.fcrawledsiteslist_bfs.append(lurlforparsing)
                self.fcrawledsiteslistforprint_bfs.append("Level: " + str(self.fcurrentlevel) + " " + lurlforparsing)
                self.fcrawledsitescount_bfs += 1

            # Write data to file only when enabled
            if self.fcanwriteurldatatofile:

                # write url page data to file
                lfilenameforurl = DIR_FOR_DATA_FILES + "/" + "BFS-" + PREFIX_FOR_URL_DATA_FILE + str(len(self.fcrawledsiteslist_bfs)) + FILE_EXT

                # add entry for url in file mapping list
                self.ffilenamesmappinglist.append("Url: " + lnodeforurl.get_url() + ",Filename: " + lfilenameforurl)
                write_to_file(lfilenameforurl, lnodeforurl.get_data())

            # increment the level and send to bfs crawler
            self.fcurrentlevel += 1

            # call the bfs crawler recursive function
            self.recurse_for_bfs(self.fcurrentlevel)

        # if no urls were crawled print default message
        if len(self.fcrawledsiteslist_bfs) == 0:
            self.fcrawledsiteslist_bfs.append("No urls crawled.")
            #self.fcrawledsiteslistforprint_bfs.append("No urls crawled.")

        # set the filename for writing the output
        if self.fcurrenttask == MODE_TASK1:
            lfilename = TASK1_FILE_CONSTANT
        elif self.fcurrenttask == MODE_TASK2:
            lfilename = TASK2_A_FILE_CONSTANT
        elif self.fcurrenttask == MODE_TASK3:
            lfilename = TASK3_FILE_CONSTANT
        else:
            lfilename = BFS_CRAWLED_PAGES_LIST

        # Create file
        lfilename = lfilename + FILE_EXT
        create_file(lfilename, '')

        # read the contents from the collections into files
        convert_data_from_collection_to_file(lfilename, self.fcrawledsiteslist_bfs)
        # convert_data_from_collection_to_file(lfilename, self.fcrawledsiteslistforprint_bfs)

        # Write data to file only when enabled
        if self.fcanwriteurldatatofile:
            convert_data_from_collection_to_file("BFS-" + FILE_FOR_URL_DATA_MAPPING + FILE_EXT, self.ffilenamesmappinglist)

        # convert_data_from_collection_to_file(QUEUED_PAGES_LIST, self.fqueuedsiteslist)

    def recurse_for_bfs(self, p_level):

        # print data for keeping track of recursion
        print "Fetching links for level: " + str(p_level)
        print "No. of links crawled: " + str(len(self.fcrawledsiteslist_bfs))

        # Exit conditions - if max level has been reached or max no. of urls have been crawled
        if (p_level > MAX_LEVEL_FOR_CRAWLING) or (len(self.fcrawledsiteslist_bfs) >= LIMIT_FOR_MAX_CRAWLED_LINKS):

            if (p_level > MAX_LEVEL_FOR_CRAWLING):
                print "Exiting as max level reached"

            if len(self.fcrawledsiteslist_bfs) >= LIMIT_FOR_MAX_CRAWLED_LINKS:
                print "Exiting as max level reached or max. no of urls crawled"

            return

        # continue till there are nodes in queue to be processed for bfs
        while len(self.fqueueforbfs) > 0:

            # get the node from the queue
            lnode = self.fqueueforbfs.popleft()

            # get the level for the new node
            lnewnodelevel = lnode.get_level() + 1

            # get the list of links for the url
            llistoflinks = lnode.get_parsed_links()

            # get list of strings for node
            # llistoflinkstrings = lnode.get_parsed_links_strings()

            lindex = 0
            for litem in llistoflinks:
            #while lindex < 10:

                #test statement for while loop
                #litem = llistoflinks[lindex]

                # test code for print link strings
                # try:
                #     litemstring = llistoflinkstrings[lindex]
                # except:
                #     litemstring = ''
                #
                # if not is_string_valid(litemstring):
                #     litemstring = ''

                # crawl url only if it has not already been crawled, the max level has not yet been crossed and max no. of urls have not been crawled
                if (litem not in self.fcrawledsiteslist_bfs) and \
                        (lnewnodelevel <= MAX_LEVEL_FOR_CRAWLING) and \
                            (len(self.fcrawledsiteslist_bfs) < LIMIT_FOR_MAX_CRAWLED_LINKS):

                    #print "Fetching data for url no: " + str(lindex)

                    # Time delay as per the politeness policy - Delay of 1 second
                    time.sleep(DELAY_FOR_PARSING)

                    # get the crawled node for the url
                    litemnode = self.flinkparser.parse_using_bsoup(litem, lnewnodelevel)

                    if litemnode is not None:

                        # add the item for the child url node to queue
                        self.fqueueforbfs.append(litemnode)

                        # add child url to crawled sites list
                        self.fcrawledsiteslist_bfs.append(litem)
                        #self.fcrawledsiteslistforprint_bfs.append("Level: " + str(lnewnodelevel) + " url:" + litem + " linkstring:" + litemstring)
                        self.fcrawledsitescount_bfs += 1

                        # Write data to file only when enabled
                        if self.fcanwriteurldatatofile:

                            # write url page data to file
                            lfilenameforurl = DIR_FOR_DATA_FILES + "/" + "BFS-" +PREFIX_FOR_URL_DATA_FILE + str(len(self.fcrawledsiteslist_bfs)) + FILE_EXT

                            # add entry for url in file mapping list
                            self.ffilenamesmappinglist.append("Url: " + litemnode.get_url() + ",Filename: " + lfilenameforurl)
                            write_to_file(lfilenameforurl, litemnode.get_data())

            lindex += 1

            # recurse again for next level
            self.recurse_for_bfs(lnode.get_level()+1)

    def crawl_dfs(self):

        lurlforparsing = self.fseedurl

        # remove contents from file mapping list
        del self.ffilenamesmappinglist[:]

        self.fcurrentlevel = 1

        # get node for seed url
        lnodeforurl = self.flinkparser.parse_using_bsoup(lurlforparsing, self.fcurrentlevel)

        if lnodeforurl is not None:

            # add the node to the stack for dfs crawling
            self.fstackfordfs.append(lnodeforurl)

            # add seed url to crawled sites list
            if lurlforparsing not in self.fcrawledsiteslist_dfs:
                self.fcrawledsiteslist_dfs.append(lurlforparsing)
                #self.fcrawledsiteslistforprint_dfs.append("Level: " + str(self.fcurrentlevel) + " " + lurlforparsing)
                self.fcrawledsitescount_dfs += 1

            # Write data to file only when enabled
            if self.fcanwriteurldatatofile:

                # write url page data to file
                lfilenameforurl = DIR_FOR_DATA_FILES + "/" + "DFS-" + PREFIX_FOR_URL_DATA_FILE + str(len(self.fcrawledsiteslist_dfs)) + FILE_EXT

                # add entry for url in file mapping list
                self.ffilenamesmappinglist.append("Url: " + lnodeforurl.get_url() + ",Filename: " + lfilenameforurl)
                write_to_file(lfilenameforurl, lnodeforurl.get_data())

            self.fcurrentlevel += 1

            # call the dfs crawling recursive function
            self.recurse_for_dfs(self.fcurrentlevel)

        # if no urls have been add default message
        if len(self.fcrawledsiteslist_dfs) == 0:
            self.fcrawledsiteslist_dfs.append("No urls crawled.")
            #self.fcrawledsiteslistforprint_dfs.append("No urls crawled.")

        # read the contents from the collections into files
        if self.fcurrenttask == MODE_TASK2:
            lfilename = TASK2_B_FILE_CONSTANT
        else:
            lfilename = DFS_CRAWLED_PAGES_LIST

        # create file for list of urls
        lfilename = lfilename + FILE_EXT
        create_file(lfilename, '')

        # print the list of crawled urls for dfs to file
        convert_data_from_collection_to_file(lfilename, self.fcrawledsiteslist_dfs)
        #convert_data_from_collection_to_file(lfilename, self.fcrawledsiteslistforprint_dfs)

        # Write data to file only when enabled
        if self.fcanwriteurldatatofile:
            convert_data_from_collection_to_file("DFS-" + FILE_FOR_URL_DATA_MAPPING + FILE_EXT, self.ffilenamesmappinglist)

        # convert_data_from_collection_to_file(QUEUED_PAGES_LIST, self.fqueuedsiteslist)

    def recurse_for_dfs(self, p_level):

        # print data for keeping track of recursion
        print "Fetching links for level: " + str(p_level)
        print "No. of links crawled: " + str(len(self.fcrawledsiteslist_dfs))

        # Exit conditions - stop recursion if max urls have been crawled or max level has been reached
        if (p_level > MAX_LEVEL_FOR_CRAWLING) or (len(self.fcrawledsiteslist_dfs) >= LIMIT_FOR_MAX_CRAWLED_LINKS):
            if (p_level > MAX_LEVEL_FOR_CRAWLING):
                print "Exiting as max level reached"

            if len(self.fcrawledsiteslist_dfs) >= LIMIT_FOR_MAX_CRAWLED_LINKS:
                print "Exiting as max level reached or max. no of urls crawled"

            return

        while len(self.fstackfordfs) > 0:

            # get the node from the stack for dfs
            lnode = self.fstackfordfs.pop()

            # get the level for the new node
            lnewnodelevel = lnode.get_level() + 1

            # get the list of links for the url
            llistoflinks = lnode.get_parsed_links()

            # get list of strings for node
            #llistoflinkstrings = lnode.get_parsed_links_strings()

            lindex = 0
            for litem in llistoflinks:
            #while lindex < 2:

                #test statement for while loop
                #litem = llistoflinks[lindex]

                # test code for printing the anchor text
                #try:
                #    litemstring = llistoflinkstrings[lindex]
                # except:
                #     litemstring = ''
                #
                # if not is_string_valid(litemstring):
                #     litemstring = ''

                # crawl the child links if only it has not been crawled before, max no. of urls have not been crawled and max level has not reached
                if (litem not in self.fcrawledsiteslist_dfs) and \
                        (lnewnodelevel <= MAX_LEVEL_FOR_CRAWLING) and \
                        (len(self.fcrawledsiteslist_dfs) < LIMIT_FOR_MAX_CRAWLED_LINKS):

                    # print "Fetching data for url no: " + str(lindex)

                    # Time delay as per the politeness policy - Delay of 1 second
                    time.sleep(DELAY_FOR_PARSING)

                    # get the crawled node for the child url
                    litemnode = self.flinkparser.parse_using_bsoup(litem, lnewnodelevel)

                    if litemnode is not None:

                        # add the crawled item node to stack
                        self.fstackfordfs.append(litemnode)

                        # add seed url to crawled sites list
                        self.fcrawledsiteslist_dfs.append(litem)
                        #self.fcrawledsiteslistforprint_dfs.append("Level: " + str(lnewnodelevel) + " url:" + litem + " linkstring:" + litemstring)
                        self.fcrawledsitescount_dfs += 1

                        # Write data to file only when enabled
                        if self.fcanwriteurldatatofile:

                            # write url page data to file
                            lfilenameforurl = DIR_FOR_DATA_FILES + "/" + "BFS-" + PREFIX_FOR_URL_DATA_FILE + str(len(self.fcrawledsiteslist_dfs)) + FILE_EXT

                            # add entry for url in file mapping list
                            self.ffilenamesmappinglist.append("Url: " + litemnode.get_url() + ",Filename: " + lfilenameforurl)
                            write_to_file(lfilenameforurl, litemnode.get_data())

                        # Proper DFS - this should crawl from first node itself upto its hierarchy
                        self.recurse_for_dfs(lnode.get_level() + 1)

            lindex += 1

            # this will crawl from last node in stack - Reverse DFS
            #self.recurse_for_dfs(lnode.get_level()+1)
