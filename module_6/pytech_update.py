# pytech_update
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

# connecting to collection for student documents
students = db.students

#using find() to get all 
docs = students.find({})

# output for find()
print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name: ", doc["last_name"])
    print()


# using update_one to change last name entry for student 1007
result= students.update_one({"student_id": 1007}, {"$set": {"last_name": "Oakenshield, son of Thrain "}})


# using find.one() to get single 
student = students.find_one({"student_id": "1007"})


#output for updated
print()
print("--DISPLAYING STUDENT DOCUMENT 1007--")
print("Student ID: ", student["student_id"]) 
print("First Name: ", student["first_name"])
print("Last Name: ", student["last_name"])

print("\n\n End of Program, press any key to continue...")
