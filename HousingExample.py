'''
    Here is a very simple example that
    graphs prices with plotly, along
    with the craigslist api.
'''
from craigslist import *
#from bs4 import BeautifulSoup
from util import *

import requests
import plotly
import plotly.plotly as py
import plotly.graph_objs as go



plotly.tools.set_credentials_file(
    username="gregv21v",
    api_key="8b7n55ydz9"
)
houses = CraigslistHousing(
    site="boston", # Site is the city, I think.
    filters={
        "search_distance" : 100
    }
)

traces = [];
#f = open("urls.txt", "w")
indices = [0];
prices = [];
for result in houses.get_results(limit=5):

    print str(result)
    #f.write(result["url"] + "\n")
    prices.append(result["price"])

    attrs = get_attrs(result)


    indices.append(indices[len(indices) - 1] + 0.1)


data = [
    go.Scatter(
        x = indices,
        y = prices,
        mode = "markers"
    )
]

plotly.offline.plot({
    "data" : data,
    "layout" : go.Layout(title="hello world")
})
f.close()
