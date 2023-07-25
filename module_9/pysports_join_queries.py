""" 
    Title: pysports_join_queries.py
    Author: Heather Larnach
    Date: July 25, 2023
    Description: join for pysports
"""




import mysql.connector 
from mysql.connector import errorcode

#db config
config = {
    "user": "pysports_user",
    "password": "MySQL8ISOkay!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try:
    """ try/catch block for errors """ 

    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    # inner join 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # getting results 
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    # how to display 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ in case of errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()