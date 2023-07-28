""" 
    Title: pysports_update_and_delete.py
    Author: Heather Larnach
    Date: July 26, 2023
    Description: update and delete for pysports
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


def all_players(cursor, title):


    # inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get players
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # how to display results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 


    cursor = db.cursor()

    # insert player  
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # player fields 
    player_data = ("Smeagol", "Shire Folk", 1)

    # insert a new record into player
    cursor.execute(add_player, player_data)

    # committing 
    db.commit()

    # display all records in the player
    all_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # update the new insert
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # execute update
    cursor.execute(update_player)
    

    # display all records in player 
    all_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # delete 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    # display all records in the player 
    all_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to db """

    db.close()