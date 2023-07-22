""" 
    Title: pysports-queries.py
    Author: Heather Larnach
    Date: July 20, 2023
    Description: queries for pysports
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
    """ try/catch block for error """ 

    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    # select query from team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
 
    # getting results
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # how to handle and display
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # select query for player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # getting results
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # how to handle and display
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3], player[4], player[5]))

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