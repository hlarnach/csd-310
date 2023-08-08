""" 
    Title: what_a_book.py
    Author: Heather Larnach
    Date: August 6 2023
    Description: WhatABook final project
"""

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

# database config 
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n     Main Menu ")

    print("    1. View Books")   
    print("    2. View Store Locations")
    print("    3. My Account")
    print("    4. Exit Program")
    try:
        choice = int(input('\n\n  Enter Selection: '))

        return choice
    except ValueError:
        print("\n  Invalid selection, thank you and have a great day...\n")

        sys.exit(0)

def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # get results 
    books = _cursor.fetchall()

    print("\n     AVAILABLE BOOKS")
    
    # how to display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n     DISPLAYING STORE LOCATIONS")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))


# making sure the account number is valid
def check_user():

    try:
        user_id = int(input('\n      Enter Your Customer ID number: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, thank you and have a great day...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid selection, thank you and have a great day...\n")

        sys.exit(0)

# display the user menu
def show_account_menu():

    try:
        print("\n      Customer Menu")
        print("        1. Wishlist")
        print("        2. Add Book")
        print("        3. Main Menu")
        account_option = int(input('\n\n  Enter Selection: '))

        return account_option
    except ValueError:
        print("\n  Invalid selection, thank you and have a great day...\n")

        sys.exit(0)

#list of books added to the users wishlist
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n          DISPLAYING WISHLIST ITEMS ")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

#list of books not in the users wishlist
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n                AVAILABLE BOOKS")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    #error handling in case of database error

    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor() # cursor for MySQL queries

    print("\n  Welcome to the WhatABook App! ")

    user_selection = show_menu() # show the main menu 

    #the user's selection is not 4
    while user_selection != 4:

        # user selection is option 1, display all books
        if user_selection == 1:
            show_books(cursor)

        # if the user selection is option 2, display all locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selection is option 3, \validate the entered user_id and display user menu
        if user_selection == 3:
            my_user_id = check_user()
            account_option = show_account_menu()

            while account_option != 3:

                # if the user selection is option 1, show user wish list
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selection is option 2, show books not currently in the users wishlist
                if account_option == 2:

                    show_books_to_add(cursor, my_user_id)

                    # prompt to add book
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit changes to whatabook wishlist and confirm to user 

                    print("\n        Book id: {} was successfully added to your wishlist!".format(book_id))

                # if the selected option is < 0 or > 3, display invalid selection message
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid selection, please try again...")

                # show account menu 
                account_option = show_account_menu()
        
        # if the user selection is < 0 or > 4, display an invalid selection message
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid selection, please try again using one of the options above...")
            
        # show the main menu
        user_selection = show_menu()

    print("\n  Thank you for using the Whatabook App and have a great day...")

except mysql.connector.Error as err:
    #error handling 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are not valid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()