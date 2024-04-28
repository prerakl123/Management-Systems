-- MySQL Distrib 5.7.44, for Windows (x86_64)
--
-- Host: 127.0.0.1    Database: library
-- ------------------------------------------------------
-- Server version	5.7.44


--
-- Table structure for table `books`
--
CREATE TABLE IF NOT EXISTS books(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    title            VARCHAR(255)    NOT NULL,
    authorid          INTEGER(11)    NOT NULL,
    genreid           INTEGER(11)        NULL,
    publication_year         DATE    NOT NULL,
    isbn             VARCHAR(255)    NOT NULL,
    availability     INTEGER(100)    NOT NULL,
    shelfid           INTEGER(11)    NOT NULL
);


--
-- Table structure for table `authors`
--
CREATE TABLE IF NOT EXISTS authors(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    name             VARCHAR(255)    NOT NULL,
    nationality      VARCHAR(255)        NULL
);


--
-- Table structure for table `shelf`
--
CREATE TABLE IF NOT EXISTS shelf(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    location         VARCHAR(255)    NOT NULL
);


--
-- Table structure for table `genre`
--
CREATE TABLE IF NOT EXISTS genre(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    name             VARCHAR(255)    NOT NULL
);


--
-- Table structure for table `librarian`
--
CREATE TABLE IF NOT EXISTS librarian(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    name             VARCHAR(255)    NOT NULL,
    username         VARCHAR(255)    NOT NULL,
    passhash         VARCHAR(255)    NOT NULL
);


--
-- Table structure for table `borrowed_books`
--
CREATE TABLE IF NOT EXISTS borrowed_books(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    bookid            INTEGER(11)    NOT NULL,
    memberid          INTEGER(11)    NOT NULL,
    borrow_date              DATE    NOT NULL,
    return_date              DATE    NOT NULL,
    returned                 BOOL    NOT NULL    DEFAULT FALSE
);


--
-- Table structure for table `transactions`
--
CREATE TABLE IF NOT EXISTS transactions(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    borrowid          INTEGER(11)    NOT NULL,
    librarianid       INTEGER(11)    NOT NULL,
    fine              INTEGER(11)    NOT NULL
);


--
-- Table structure for table `members`
--
CREATE TABLE IF NOT EXISTS members(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    name             VARCHAR(255)    NOT NULL,
    email            VARCHAR(255)    NOT NULL,
    address                  TEXT    NOT NULL,
    phno             VARCHAR(255)    NOT NULL
);


--
-- Table structure for table `reviews`
--
CREATE TABLE IF NOT EXISTS reviews(
	id                INTEGER(11)    NOT NULL    PRIMARY KEY    AUTO_INCREMENT,
    memberid          INTEGER(11)    NOT NULL,
    bookid            INTEGER(11)    NOT NULL,
    rating            INTEGER(10)    NOT NULL,
    review                   TEXT        NULL
);


--
-- FOREIGN KEY ASSIGNMENT
--
ALTER TABLE books ADD FOREIGN KEY(authorid) REFERENCES authors(id);
ALTER TABLE books ADD FOREIGN KEY(genreid) REFERENCES genre(id);
ALTER TABLE books ADD FOREIGN KEY(shelfid) REFERENCES shelf(id);

ALTER TABLE borrowed_books ADD FOREIGN KEY(bookid) REFERENCES books(id);
ALTER TABLE borrowed_books ADD FOREIGN KEY(memberid) REFERENCES members(id);

ALTER TABLE transactions ADD FOREIGN KEY(borrowid) REFERENCES borrowed_books(id);
ALTER TABLE transactions ADD FOREIGN KEY(librarianid) REFERENCES librarian(id);

ALTER TABLE reviews ADD FOREIGN KEY(memberid) REFERENCES members(id);
ALTER TABLE reviews ADD FOREIGN KEY(bookid) REFERENCES books(id);