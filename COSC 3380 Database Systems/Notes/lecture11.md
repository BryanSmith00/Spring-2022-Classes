# Database Systems Lecture 11

## Entity integrity constraint
---
* Every row in a table in unique
* No primary key value can be NULL
* Used for identification of individual tuples in a relation
* Ensures ability to distinguish tuples when referenced from other relations

## Referential Inegrity Constraint
---
* Specified between two relations
* Maintains consistency among tuples in two relations
* A tuples in one relation that refers to another relation must refer to a relation that exists

## Foreign keys
---
* A set of attributes FK in R<sub>1</sub> have the same domain(s) as the primary key attributes PK in R<sub>2</sub>
* Value of FK in a tuple t<sub>1</sub> of the current state r<sub>1</sub> either occurs as a value of PK for some tuple t<sub>2</sub> in the current state r<sub>2</sub> or is NULL

The Foreign key is about building relationships<br>
foreign key references the primary key of another relation

## Semantic Constraints
---

 * May have to be specified and enforces on a relational database


## Triggers and Assertions
---

* Defined in the DBMS but enforced in the application 

## State Constraints
---

* Define the constraints that a valid state of the database must satisfy

## Transition Constraints
---

* Define to deal with state changes in the database
* eg. salary of an employee cannot decrease
* Enforced by application programs

## Functional Dependency Constraint
---
* Establishes a functional relationship among two sets of attributes X and Y
* Value of X determines a unique value of Y
*  Enforced using validation checks<br></br>

## Update operations
---

In The case of integrity violation several actions can be taken
* Cancel the operation that causes the violation (RESTRICT or REJECT operation)
* Perform the operation but inform the user of the violation
* Trigger additional updates so the violation is corrected (CASCADE option, SET NULL option)
* Execute a user-specified error-correction routine
