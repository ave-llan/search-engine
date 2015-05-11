from sys import argv
import urllib
from urlparse import urljoin

script, seedPage = argv


#HELPER FUNCTIONS
# appends elements of q to p if not already in p
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

#splits a string using all characters specified in splitlist (a string of characters)
def split_string(source,splitlist):
    output = []
    atsplit = True # At a split point from splitlist
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else: 
                #add char to last word
                output[-1] = output[-1] + char
    return output


# tries to read a page and return the contents
def read_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

# returns the first link on a page
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

# returns a list of all links on a page
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


# mutates a provided index
# if keyword already in index, adds url to the keyword's list of urls
# else adds the keyword with its url to the index
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

# returns a list of urls associated with the given keyword
# if keyword not in index, returns an empty url
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

# extracts keywords from a page and adds them to the index with associated page
def add_page_to_index(index, url, content):
    keywords = content.split()
    for keyword in keywords:
        add_to_index(index, keyword, url)

# returns an index after crawling pages reachable from seed page
def crawl_web(seed):
    count = 0
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        print count, page
        count += 1
        if page not in crawled:
            content = read_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index



foundLinks = crawl_web(seedPage)
for link in foundLinks:
    print link