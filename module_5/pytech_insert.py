# importing my mongodb
from pymongo.mongo_client import MongoClient

# url for connection
url = "mongodb+srv://admin:admin@cluster0.fnorldu.mongodb.net/?retryWrites=true&w=majority"

# connect to cluster0
client = MongoClient(url)

#connecting to my db
db = client.pytech

students = db.students

"new students docs and insert.one statements"

thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield"
}
thorin_student_id = students.insert_one(thorin).inserted_id

bilbo= {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
}
bilbo_student_id = students.insert_one(bilbo).inserted_id

frodo= {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins"
}
frodo_student_id = students.insert_one(frodo).inserted_id



#output showing doc id numbers

print(" --INSERT STATEMENTS--")
print(" Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))
print(" Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))
print(" Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))
input("\n\n End of program, press any key to exit...")