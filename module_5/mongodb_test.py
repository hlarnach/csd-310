"""
mongodb_test
Heather Larnach
28 June 2023
CYBR 410

"""


# importing my mongodb
from pymongo.mongo_client import MongoClient

# url for connection
url = "mongodb+srv://admin:admin@cluster0.fnorldu.mongodb.net/?retryWrites=true&w=majority"

# connect to cluster0
client = MongoClient(url)

#connecting to my db
db = client.pytech

#printing in the proper format...
#also weird that the O is capital??? but it matches so...
print("--Pytech COllection List--")
print(db.list_collection_names())

# needs an end
input("End of program, press any key to exit...")




