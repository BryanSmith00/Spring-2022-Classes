# Database Lecture 13
Week 7 Tuesday

## CREATE Command
---

* CREATE SCHEMA statement - CREATE TABLE COMPANY

* CREATE TABLE Command - CREATE TABLE COMPANY.slsls


## CREATE TABLE Command
---
* Base Relations (base tables) - Stored directly in the DBMS
* Virtual relations - Views that you can create with view command, dynamically created, not stored in dbms


Why do we need Views (Virtual relations)?
* Helps provide abstraction, prodivde indirect access to a table, keeps people from seeing too much
* Functionality, controlling access to what people see, security<br></br>


Some relationships are implemented as entitity tables in implementation<br></br>

Domains are like constraint variables allow you to set a type in 1 location and use it everywhere<br></br>

## Column Constraints
---
* PRIMARY KEY
* FOREIGN KEY
* UNIQUE
* NOT NULL
* DEFAULT
* CHECK

## DROP and ALTER Command
---
DROP command can be used to drop or remove database objects
* Can be combined with CASCADE and RESTRICT
* Ex. DROP SCHEMA purchase CASCADE - deletes everything as is
* Ex. DROP SCHEMA purchase RESTRICT - Checks with you to empty tables before dropping

ALTER statement can be used to modify table column definitions
* Ex. ALTER TABLE product ADD prodimage BLOB
* Ex. ALTER TABLE supplier ALTER supstatus SET DEFAULT '10'<br></br>

## SQL Data Manipulation Language (DML)
---
SELECT command<br>
INSERT command<br>
DELETE command<br>
UPDATE command<br>

## SELECT Statement
---
Basic information retrieval tool<br>
Result of SQL SELECT Statement is a multiset not a set!<br>

### Multiset (bag behavior) - think shopping bag
* Elements are not ordered and there can be duplicates

Duplication elimination is expensive<br>
User may want to see duplicate tuples<br>

Tuple-id may be used as a key


## Basic SQL Queries
---
### SELECT-FROM-WHERE Structure
SELECT &lt;attribute list<br>
FROM &lt;table list<br>
WHERE &lt;condition<br>

Logical comparison operators 

Projection attributes
* Attributes whose values are to be retrieved

Selection conditions
* Boolean conditions that must be true for any retreived tuple
* Join conditions?<br></br>

### DISTINCT keyword
SELECT DISTINCT columnname - returns no duplicate items<br></br>

Create a new data item with a SELECT query<br>
does not store it into the database


## WHERE clause - simple queries