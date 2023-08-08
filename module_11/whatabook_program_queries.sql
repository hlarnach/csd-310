/*
    Title: whatabook_program_queries.sql
    Author: Heather Larnach
    Date: August 5, 2023
    Description: WhatABook program queries for wk 11
*/

--Select query to view a users wishlist items 
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = --enter the user id number;


--Select query to view the store's location 
SELECT store_id, locale from store;


--Select query to view a full listing of the books WhatABook offers
SELECT book_id, book_name, author, details from book;



--Select query to view a listing of books not already in your a users wishlist.
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = --enter the user id number);


--Insert statement to add a new book to a users wishlist. 
INSERT INTO wishlist(user_id, book_id)
    VALUES(--enter user id number , book id numbers(s))



--Remove a book from the user's wishlist.
DELETE FROM wishlist WHERE user_id = --enter user id number AND book_id = --enter book id number(s);