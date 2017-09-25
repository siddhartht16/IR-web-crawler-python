"""
This class will define a link parser required to parse input html and return collection of specified tag
"""
from bs4 import BeautifulSoup
import urllib2
from consts import *
from utils import *
from collections import deque
import sys

class cnode:
    def __init__(self, p_level, p_url, p_data, p_parsedlinks, p_parsedlinksstrings):
        self.flevel = p_level
        self.furl = p_url
        self.fdata = p_data
        self.fparsedlinks = p_parsedlinks
        self.fparsedlinksstrings = p_parsedlinksstrings

    def get_level(self):
        return self.flevel

    def get_url(self):
        return self.furl

    def get_data(self):
        return self.fdata

    def get_parsed_links(self):
        return self.fparsedlinks

    def get_parsed_links_strings(self):
        return self.fparsedlinksstrings


class LinkParserClass:
    # set that will contain all the links found for the tag

    def __init__(self, p_owner):
        self.fsoup = None
        self.furl_to_parse = ''
        self.furl_page = None
        self.fowner = p_owner
        self.fnodeforurl = None
        self.furllevel = 0

        # references to control filtering
        self.fcanapplyfilter = False
        self.ffiltertext = ''

    def reset(self):
        self.fsoup = None
        self.furl_to_parse = ''
        self.furl_page = None
        self.furl_page_data = ''
        self.fnodeforurl = None
        self.furllevel = 0

        # references to control filtering
        self.fcanapplyfilter = False
        self.ffiltertext = ''

    def parse_using_bsoup(self, p_url, p_level):

        # get url before sending request
        p_url = get_complete_url(WIKI_DOMAIN_NAME, p_url)

        self.furl_to_parse = p_url

        #print "Getting data for url: " + p_url
        # print "At level: " + str(self.fowner.fcurrentlevel)

        try:

            # open the url and get the document object
            self.furl_page = urllib2.urlopen(p_url)

            self.furl_page_data = self.furl_page.read()

            self.fsoup = None

            # get the soup using BeautifulSoup api
            #self.fsoup = BeautifulSoup(self.furl_page.read(), "html.parser")
            self.fsoup = BeautifulSoup(self.furl_page_data, "html.parser")

            self.furllevel = p_level

            # parse the soup and return the set of links that can be retrieved from the page document
            lnode = self.parse_soup()

            return lnode
        except:
            print "Unexpected error:", sys.exc_info()[0]
            return None

    def parse_soup(self):
        # initialise the counter to zero to start with
        key_counter = 0

        # list to maintain unique items
        ltemplistforuniquehref = []
        # ltemplistforlinkstring = []

        # get the outermost div element containing the content
        # llistofanchorlinks = self.fsoup.select("div[id='content'] a")
        llistofanchorlinks = self.fsoup.select("p a")

        # iterate over all the anchor links and add them to list after only they meet the filter criteria
        for llink in llistofanchorlinks:

            # get link href
            llinkhref = llink.get("href")
            llinkstring =  llink.string

            if not can_add_link(llinkhref):
                continue

            if self.fcanapplyfilter:
                if not contains_keyword( self.ffiltertext,llink):
                    continue

            key_counter += 1
            if WIKI_DOMAIN_NAME not in llinkhref:
                llinkhref = WIKI_DOMAIN_NAME + llinkhref

            if llinkhref not in ltemplistforuniquehref:
                ltemplistforuniquehref.append(llinkhref)
                # ltemplistforlinkstring.append(llinkstring)

        # print "No. of links parsed: " + str(len(ltemplistforuniquehref))

        # create object of node and add it to the list
        self.fnodeforurl = cnode(self.furllevel,
                                 self.furl_to_parse,
                                 self.furl_page_data,
                                 ltemplistforuniquehref,
                                 ''# ltemplistforlinkstring
                                 )

        return self.fnodeforurl

    def get_data_for_url(self):
        return self.furl_page.get_text()

    def set_filter_text(self, p_filtertext):
        if is_string_valid(p_filtertext):

            # set the filter criteria
            self.fcanapplyfilter = True
            self.ffiltertext = p_filtertext

