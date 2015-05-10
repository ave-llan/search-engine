from sys import argv
import urllib2
from urlparse import urljoin

script, seedPage = argv

# appends elements of q to p if not already in p
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

# returns the html of a page from given url
def read_page(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()

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
def add_to_index(index,keyword,url):
    # if in index, add url
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

# returns a list of urls associated with the given keyword
# if keyword not in index, returns an empty url
def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

# extracts keywords from a page and adds them to the index with associated page
def add_page_to_index(index, url, content):
    keywords = content.split()
    for keyword in keywords:
        add_to_index(index, keyword, url)

# returns an index after crawling pages reachable from seed page
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while to_be_crawled:
        page = to_be_crawled.pop()
        if page not in crawled:
            content = read_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index



foundLinks = crawl_web(seedPage)
for link in foundLinks:
    print link