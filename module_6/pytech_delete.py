# pytech_delete
# Heather Larnach
# 5 July 2023
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

# output for find()
print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name: ", doc["last_name"])
    print()

# new student info
sam = {
    "student_id": "1010",
    "first_name": "Samwise",
    "last_name": "Gamgee"
}

# insert new student
sam_student_id = db.students.insert_one(sam).inserted_id

#output showing inserted student
print(" --INSERT STATEMENTS--")
print(" Inserted student record into the students collection with document_id " + str(sam_student_id))

# using find.one() to get single 
student = db.students.find_one({"student_id": "1010"})

#output for updated
print()
print("--DISPLAYING STUDENT TEST DOC--")
print("Student ID: ", student["student_id"]) 
print("First Name: ", student["first_name"])
print("Last Name: ", student["last_name"])
print()

# deleting poor Sam
del_student = db.students.delete_one({"student_id": "1010"})


#using find() to get all 
docs = db.students.find({})

# output for find()
print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name: ", doc["last_name"])
    print()

# close
print("\n\n End of Program, press any key to continue...")