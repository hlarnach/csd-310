# 
# pytech_queries
# Heather Larnach
# 29 June 2023
# CYBR 410


# importing my mongodb
from pymongo.mongo_client import MongoClient

# url for connection
url = "mongodb+srv://admin:admin@cluster0.fnorldu.mongodb.net/?retryWrites=true&w=majority"

# connect to cluster0
client = MongoClient(url)

#connecting to my db
db = client.pytech

#using find() to get all 
docs = db.students.find({})



print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name: ", doc["last_name"])
    print()

#using find.one() to get single 
student = db.students.find_one({"student_id": "1008"})

#output
print()
print("--DISPLAYING STUDENT DOC FROM find_one() QUERY--")
print("Student ID: ", student["student_id"]) 
print("First Name: ", student["first_name"])
print("Last Name: ", student["last_name"])

print("\n\n End of Program, press any key to continue...")