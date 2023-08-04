/*
    Title: whatabook.init.sql
    Author: Heather Larnach
    Date: August 3, 2023
    Description: Whatabook init script.
*/

-- drop test user incase present
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create a new whatabook_user 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!'; 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop constraints if present
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if present 
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


--create user table
CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

--create book table
CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);


--create wishlist table
CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

--create store table
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);


--store info
INSERT INTO store(locale)
    VALUES('123 Bookstore Lane Page, AZ 86036');


--insert 9 books 
INSERT INTO book(book_name, author, details)
    VALUES('Fantastic Beasts and Where to Find Them', 'Newt Scamander', 'The essential guide to magical beasts by the renowned magizoologist');

INSERT INTO book(book_name, author, details)
    VALUES('Quidditch Through the Ages', 'Kennilworthy Whisp', 'History of the wizarding worlds favorite sport');

INSERT INTO book(book_name, author, details)
    VALUES('The Monster Book of Monsters', 'Edwardus Lima', 'A guide book for the care of magical creatures, see shopkeeper for assistance');

INSERT INTO book(book_name, author, details)
    VALUES('Unfogging the Future', 'Cassandra Vablatsky', 'Instructional guide for the less than precise science of divination');

INSERT INTO book(book_name, author, details)
    VALUES('History of Magic', 'Bathilda Bagshot', 'A complete wizarding history up to the end of the 19th century');

INSERT INTO book(book_name, author, details)
    VALUES('Break with a Banshee', 'Gilderoy Lockhart', 'An account of the banishing of the Bandon Banshee by five time winner of Witch Weeklys Most-Charming Smile Award');

INSERT INTO book(book_name, author, details)
    VALUES('Magick Moste Evile', 'Godelot', 'Its best we dont mention the contents of this volume');

INSERT INTO book(book_name, author, details)
    VALUES('Hogwarts: A History', 'Bathilda Bagshot', 'A comprehensive account of the schools illustrious history, however does not contain mention of house elves');

INSERT INTO book(book_name, author, details)
    VALUES('The Tales of Beedle the Bard', 'Beedle the Bard', 'A collection of popular childrens bedtime stories');

--insert 3 users
INSERT INTO user(first_name, last_name) 
    VALUES('Harry', 'Potter');

INSERT INTO user(first_name, last_name)
    VALUES('Hermione', 'Granger');

INSERT INTO user(first_name, last_name)
    VALUES('Ronald', 'Weasley');


--insert 3 wishlists for users
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harry'), 
        (SELECT book_id FROM book WHERE book_name = 'Quidditch Through the Ages')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Hermione'),
        (SELECT book_id FROM book WHERE book_name = 'Hogwarts: A History')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Ronald'),
        (SELECT book_id FROM book WHERE book_name = 'The Tales of Beedle the Bard')
    );