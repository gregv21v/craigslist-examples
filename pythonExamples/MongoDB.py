'''
    Here is an example that shows
    how you can create a history
    of craigslist data.
'''

from pymongo import MongoClient
from craigslist import *

client = MongoClient(
            'mongodb://bari:bostonresearch@ds147975.mlab.com:47975/craigslist'
         )

db = client.get_default_database()

dataStore = db["housingData"]



# fill the database with housing data
houses = CraigslistHousing(
    site="boston", # Site is the city, I think.
    filters={
        "search_distance" : 100
    }
)


for result in houses.get_results(limit=100):
    dataStore.insert_one(result)










client.close()
