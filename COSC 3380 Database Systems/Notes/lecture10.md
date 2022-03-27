# Database Lecture 10

Relational data model and relational database constraints <br></br>

## Characteristics of relations
---
Ordering Tuples in a relation <br>
&emsp; &emsp; Elements have no order among them, but keep them in a human readable order <br> </br>

Values and NULLs in tuples <br>
Multivalued attributes must be represented by separate relations (flat model)<br></br>
Null - You don't need it or you didn't collect it <br></br>

## Relational model Notation
---

Relation schema R of degree n <br>
Denoted by R(A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>n</sub>)

Entities <br>
&emsp;All caps <br>

Dot Notation connects attribute to entity <br>
&emsp;eg. STUDENT.Name, STUDENT.SSN <br></br>

## Relational Model Constraints
---
Inherent Constraints (implicit) <br>
&emsp;eg. multivalued attributes <br>

Schema-Based Constraints (explicit) <br>

Domain constraints, key constraints, constraints on NULLs, entity integrity constraints, referential integrity constraints <br>

Application-based or semantic constraints or business rules <br>
&emsp;cannot be expressed by the schema. Enforced by the application program <br>

Domain constraints typically include <br>
&emsp;Information about the data type, length of input, etc. <br>

Key Constraints <br>
No two tuples can have the same combination of values for all their attributes <br>

<i>Superkey</i> <br>
* No two distinct tuples in any state r of R can have same values for a subset of attributes SK
* Such a subset SK is the Superkey of R
* Specifies a uniqueness constraint
* Every relation has at least one default superkey
* Superkeys can have redundant attributes
* Superkeys can be a single attribute

<b>Key</b><br>
* Superkey of R
* Property: removing any attribute A from key K leaves a set of attributes that is not a superkey of R any more<br>
* No Redundancy<br>
* Determined from the meaning of attributes<br>
* The Property is time-invariant<br>

Key satisfies two properties:<br>
* Two distrinc tuples in any state of relation cannot have identical values for all attributes in a key
* Minimal superkey - Cannot remove any attributes and still have uniqueness constraint hold. Minimality property is required for a key but optional for a superkey
* A key is a superkey but not all superkeys are keys<br>

Candidate Keys
 * Relation schema may have more than one key

 Primary key of the relation
 * Chosen from the candidate keys
 * A single attribute or a small number of attributes
 * Underlined in ER Diagram

 Other candidate keys are designated as unique keys

 KEY ATTRIBUTES CANNOT BE NULL<br>

 Invalid state - Does not obey all integrity constraints<br>
 Valid state - Statisfies all the constraints in the defined set of integrity constraints IC
 