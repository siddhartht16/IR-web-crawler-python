
from bs4 import BeautifulSoup
import urllib2
from utils import *

'''
# open the url and get the document object
url_page = urllib2.urlopen('https://en.wikipedia.org/wiki/Sustainable_energy')

# get the soup using BeautifulSoup api
fsoup = BeautifulSoup(url_page.read(), "html.parser")

key_counter = 0

content_div = fsoup.find('div', id='content')
#print content_div
for llink in content_div.find_all('a'):

    llinkhref = llink.get("href")
    if can_add_link(llinkhref):
        key_counter += 1
        print 'Link no: ' + str(key_counter) + ' Link = ' + str(llinkhref)

print get_domain_name_from_url("https://docs.python.org/2/library/collections.html")
'''

ltemplist1 = []

ltemplist2  = convert_data_from_file_to_collection("TASK2-B.txt")
print len(ltemplist2)

for litem in ltemplist2:
    if litem not in ltemplist1:
        ltemplist1.append(litem)

print len(ltemplist1)