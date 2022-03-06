# Database lecture 14
Week 7 Thursday

### Simple queries - WHERE clause

### LIKE keyword - fuzzy search

### IS NULL check
<br></br>

## Aliasing and Renaming
SELECT E.Fname, E.Lname, S.Fname, S.Lname<br>
FROM EMPLOYEE AS E, EMPLOYEE AS S<br>
WHERE E.Super_ssn=S.Ssn<br>

