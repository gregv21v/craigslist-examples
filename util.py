import requests
from bs4 import BeautifulSoup
import bs4


# Gets the attributes of a
# a Craigslist ad, and
# returns them as an array
def get_attrs(data):
    attrs = []
    response = requests.get(data["url"])
    soup = BeautifulSoup(response.content, 'html.parser')
    attrGroups = soup.find_all("p", {"class" : "attrgroup"})

    #print str(attrGroups)

    for attrGroup in attrGroups:
        spans = attrGroup.find_all("span")
        for span in spans:
            #print span
            if len(span.contents) == 1:
                attrs.append(span.contents)
            else:
                # strip all the tags from the html
                # content
                strippedString = ""

                # create one string from the entire contents
                for child in span.children:
                    if isinstance(child, bs4.element.NavigableString):
                        strippedString += child
                    else:
                        strippedString += child.contents[0]

                attrs.append(strippedString)

    return attrs


# Gets the image urls from the
# posting
def get_img_urls(data):
    #attrs = []
    response = requests.get(data["url"])
    soup = BeautifulSoup(response.content, 'html.parser')
    thumbNails = soup.find_all("a", {"class" : "thumb"})
    thumbNailUrls = []

    for thumbNail in thumbNails:
        thumbNailUrls.append(thumbNail["href"])

    #print(thumbNailUrls)
    return thumbNailUrls
    

# find all the attrs with the
# given substring
def search_for(attrs, substring):
    found = []
    for attr in attrs:
        if not attr == None and substring in attr:
            found.append(attr)
    return found


# Takes a housing and harvest all the data from
# it, including the housing data.
def harvest_all(data):
    # go through the url and harvest the data
    # present there.
    pass
