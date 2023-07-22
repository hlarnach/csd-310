<<<<<<< HEAD

/*

    Title: db_init.sql
    Author: Heather Larnach
    Date: July 20, 2023

Wrote this myself before realizing I did not have to write it myself...
I am actually proud that it looks like I had done it exactly as it should have been done.
I am looking at it as practice. 

DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsOkay!';

GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';

DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS player;

CREATE TABLE team (
    team-id    INT         NOT NULL     AUTO_INCREMENT,
    team_name  VARCHAR(75) NOT NULL,
    mascot     VARCHAR(75) NOT NULL,
    PRIMARY KEY(team_id)
);

CREATE TABLE player (
    player-id    INT         NOT NULL     AUTO_INCREMENT,
    first_name   VARCHAR(75) NOT NULL,
    last_name    VARCHAR(75) NOT NULL,
    team_id      INT         NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY (team_id)
        REFERENCESteam(team_id)
);

INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf','White Wizards')
*/

/*
    Title: db_init.sql
    Author: Professor Krasso
    Date: 15 July 2020
    Description: pysports database initialization script.
    Title: db_init.sql
    Modified by: Heather Larnach
    Date: 21 July 2023
    Description: pysports database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database
-- modified this to match my password in test file (heather larnach) 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8ISOkay!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards');

INSERT INTO team(team_name, mascot)
    VALUES('Team Sauron', 'Orcs');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Thorin', 'Oakenshield', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Bilbo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Frodo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Saruman', 'The White', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Angmar', 'Witch-king', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
=======

/*

    Title: db_init.sql
    Author: Heather Larnach
    Date: July 20, 2023

Wrote this myself before realizing I did not have to write it myself...
I am actually proud that it looks like I had done it exactly as it should have been done.
I am looking at it as practice. 

DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsOkay!';

GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';

DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS player;

CREATE TABLE team (
    team-id    INT         NOT NULL     AUTO_INCREMENT,
    team_name  VARCHAR(75) NOT NULL,
    mascot     VARCHAR(75) NOT NULL,
    PRIMARY KEY(team_id)
);

CREATE TABLE player (
    player-id    INT         NOT NULL     AUTO_INCREMENT,
    first_name   VARCHAR(75) NOT NULL,
    last_name    VARCHAR(75) NOT NULL,
    team_id      INT         NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY (team_id)
        REFERENCESteam(team_id)
);

INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf','White Wizards')
*/

/*
    Title: db_init.sql
    Author: Professor Krasso
    Date: 15 July 2020
    Description: pysports database initialization script.
    Title: db_init.sql
    Modified by: Heather Larnach
    Date: 21 July 2023
    Description: pysports database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database
-- modified this to match my password in test file (heather larnach) 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8ISOkay!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards');

INSERT INTO team(team_name, mascot)
    VALUES('Team Sauron', 'Orcs');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Thorin', 'Oakenshield', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Bilbo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Frodo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Saruman', 'The White', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Angmar', 'Witch-king', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
>>>>>>> d69dfb825a8e9ea636b6fc89a52f20aa1599d01f
    VALUES('Azog', 'The Defiler', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));