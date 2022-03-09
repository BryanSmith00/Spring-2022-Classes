# Database Lecture 15
Week 8 Tuesday

## Simple Queries contd'
<br>
WHERE classifiers<br></br>
 BETWEEN keyword<br>
- lets you look for a range of values in a query<br></br>

IN keyword<br></br>

LIKE keyword - pattern matching
- Case insensitive
<br></br>

IS NULL keyword<br></br>

## Ambiguous Attribute Names
Same name can be used for two or more attributes in different relations
* As long as the attributes are in different relations
* Must use Dot notation to access the data<br>

ex. EMPLOYEE.Name
<br></br>

## Aliasing and Renaming
Aliases or tuple variations
* Declare alternate relations names
* Uses the AS keyword

FROM EMPLOYEE AS E - Takes data from the employee table using E as a new alias<br></br>

## CROSS PRODUCT
When you select multiple tables with unspecified WHERE clause it will give all permutations<br></br>


## DISTINCT keyword
<br>

## Tables as sets in SQL

Set Operations (No duplicates)
- UNION, EXCEPT (Difference), INTERSECT

Corresponding multiset operations (Duplicates allowed)
- UNION ALL, EXCEPT ALL, INTERSECT ALL
<br></br>

## Substring pattern mathcing & arithmetic operations
LIKE keyword<br>

By default pattern matching is not case sensitive

in MYSQL use BINARY keyword to make it sensitive
- Ex. SELECT name FROM colors WHERE name LIKE BINARY 'Gr%'
<br></br>

## Ordering of query results
Treats queries as sets so has no order by default

ORDER BY clause
- DESC - Descending order
- ASC - Ascending order
<br></br>

# Query structure so far
SELECT (attribute list)<br>
FROM (table list)<br>
WHERE (condition) (optional but strongly implied)<br>
ORDER BY (attribute list) (optional but strongly implied)