#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#
# Free System Design - The Big Archive

# Free System Design - The Big Archive

Date: May 17, 2022

By ByteByteGo - ByteByteGo.com
---
#

# System Design Questions

# System Design Questions

|Question 1: What are database isolation levels? What are they used for?|Answer: Database isolation levels define the degree to which transactions are isolated from each other. They are used to control how changes made by one transaction affect other concurrent transactions.|
|---|---|
|Question 2: What is IaaS/PaaS/SaaS?|Answer: IaaS (Infrastructure as a Service), PaaS (Platform as a Service), and SaaS (Software as a Service) are different cloud service models that offer varying levels of infrastructure, platform, and software services to users.|
|Question 3: Most popular programming languages|Answer: The most popular programming languages vary over time but currently include languages like Python, Java, JavaScript, and C++.|
|Question 4: What is the future of online payments?|Answer: The future of online payments is likely to involve increased security measures, faster transaction processing, and the adoption of new technologies like blockchain and digital wallets.|
|Question 5: What is SSO (Single Sign-On)?|Answer: SSO is a method that allows users to access multiple applications with a single set of login credentials, enhancing user experience and security.|
|Question 6: How to store passwords safely in the database?|Answer: Passwords should be securely hashed and salted before storing them in the database to protect user data from unauthorized access.|
|Question 7: How does HTTPS work?|Answer: HTTPS (Hypertext Transfer Protocol Secure) encrypts data transmitted between a client and a server, ensuring secure communication over the internet.|
|Question 8: How to learn design patterns?|Answer: Learning design patterns involves studying common solutions to recurring design problems in software development and applying them to improve code quality and maintainability.|
|Question 9: A visual guide on how to choose the right Database|Answer: Choosing the right database involves considering factors like data structure, scalability, performance requirements, and budget constraints. A visual guide can help in understanding these considerations.|
|Question 10: Do you know how to generate globally unique IDs?|Answer: Generating globally unique IDs typically involves using algorithms like UUID (Universally Unique Identifier) to create identifiers that are highly unlikely to be duplicated.|
|Question 11: How does Twitter work?|Answer: Twitter operates as a social media platform where users can post short messages called tweets, follow other users, and engage with content through likes, retweets, and replies.|
|Question 12: What is the difference between Process and Thread?|Answer: A process is an independent execution unit that contains its own memory space, while a thread is a lightweight subunit of a process that shares the same memory space.|
|Question 13: Interview Question: design Google Docs|Answer: Designing Google Docs involves creating a collaborative document editing platform that allows multiple users to work on the same document simultaneously and in real-time.|
|Question 14: Deployment strategies|Answer: Deployment strategies refer to the methods and practices used to release software updates or new features into production environments while minimizing downtime and risks.|
|Question 15: Flowchart of how slack decides to send a notification|Answer: A flowchart can visually represent the decision-making process within Slack's notification system, outlining the conditions under which notifications are triggered and sent to users.|
|Question 16: How does Amazon build and operate the software?|Answer: Amazon employs various software development methodologies and technologies to build and operate its software, focusing on scalability, reliability, and customer experience.|
|Question 17: How to design a secure web API access for your website?|Answer: Designing a secure web API access involves implementing authentication mechanisms, encryption, and authorization controls to protect data exchanged between clients and servers.|
|Question 18: How do microservices collaborate and interact with each other?|Answer: Microservices communicate with each other through APIs, messaging protocols, or event-driven architectures to achieve distributed system functionality while maintaining modularity and scalability.|
|Question 19: What are the differences between Virtualization (VMware) and Containerization (Docker)?|Answer: Virtualization creates virtual instances of entire operating systems, while containerization isolates applications and their dependencies into lightweight, portable containers.|
|Question 20: Which cloud provider should be used when building a big data solution?|Answer: Cloud providers like AWS, Google Cloud, and Azure offer specialized services and tools for big data processing, storage, and analytics, making them suitable choices for building big data solutions.|
|Question 21: How to avoid crawling duplicate URLs at Google scale?|Answer: Implementing URL canonicalization, setting proper crawl directives, and using URL parameters effectively can help prevent crawling duplicate URLs at a large scale.|
|Question 22: Why is a solid-state drive (SSD) fast?|Answer: SSDs use flash memory to store data, eliminating mechanical components found in traditional hard drives, resulting in faster read/write speeds and improved performance.|
|Question 23: Handling a large-scale outage|Answer: Handling a large-scale outage involves implementing disaster recovery plans, redundancy measures, and monitoring systems to minimize downtime and restore services quickly.|
|Question 24: AWS Lambda behind the scenes|Answer: AWS Lambda is a serverless computing service that automatically scales and executes code in response to events, abstracting infrastructure management and allowing developers to focus on code logic.|
---
#

# Tech Topics

# Technical Topics

|HTTP Evolution|HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)|
|---|---|
|Scaling Websites|How to scale a website to support millions of users?|
|DevOps|DevOps Books|
|Kafka Performance|Why is Kafka fast?|
|API Technologies|SOAP vs REST vs GraphQL vs RPC|
|Browser Functionality|How do modern browsers work?|
|Caching|Redis vs Memcached|
|Concurrency Control|Optimistic locking|
|Consistency vs Latency|Tradeoff between latency and consistency|
|Security|Cache miss attack|
|Performance Troubleshooting|How to diagnose a mysterious process that’s taking too much CPU, memory, IO, etc?|
|Cache Strategies|What are the top cache strategies?|
|Large File Upload|Upload large files|
|Redis Performance|Why is Redis so Fast?|
|Payment Systems|SWIFT payment network|
|Message Delivery Semantics|At-most once, at-least once, and exactly once|
|Data Partitioning|Vertical partitioning and Horizontal partitioning|
|Content Delivery Networks|CDN|
|Data Storage|Block storage, file storage and object storage|
|Erasure Coding|Erasure coding|
|Foreign Exchange|Foreign exchange in payment|
|DNS Lookup|Domain Name System (DNS) lookup|
|URL Navigation|What happens when you type a URL into your browser?|
|AI Development|AI Coding engine|
|Data Replication|Read replica pattern|
---
#

# Interview Questions and Topics

# Interview Questions and Topics

|Topic|Page Number|
|---|---|
|Read replica pattern|105|
|Email receiving flow|107|
|Email sending flow|109|
|Interview Question: Design Gmail|111|
|Map rendering|113|
|Interview Question: Design Google Maps|115|
|Pull vs push models|117|
|Money movement|119|
|Reconciliation|122, 131|
|Which database shall I use for the metrics collecting system?|126|
|Metrics monitoring and altering system|129|
|Big data papers|134|
|Avoid double charge|136|
|Payment security|138|
|System Design Interview Tip|139|
|Big data evolvement|140|
|Quadtree|142|
|How do we find nearby restaurants on Yelp?|144|
|How does a modern stock exchange achieve microsecond latency?|147|
|Match buy and sell orders|149|
|Stock exchange design|151|
|Design a payment system|153|
|Design a flash sale system|155|
|Back-of-the-envelope estimation|157|
---
#

# Database Isolation Levels

# Database Isolation Levels

What are database isolation levels? What are they used for?

Database isolation allows a transaction to execute as if there are no other concurrently running transactions.

Isolation Level
Read
Write

Serializable
Impossible
Impossible

Repeatable Read
Impossible
Probably

Read Committed
Impossible
Probably

Read Uncommitted
Probably
Probably

Serializable: This is the highest isolation level. Concurrent transactions are guaranteed to be executed in sequence.

Repeatable Read: Data read during the transaction stays the same as the transaction starts.

Read Committed: Data modification can only be read after the transaction is committed.
---
#

# Isolation Levels in Database Transactions

# Isolation Levels in Database Transactions

Read Uncommitted: The data modification can be read by other transactions before a transaction is committed.

The isolation is guaranteed by MVCC (Multi-Version Consistency Control) and locks.

The diagram below takes Repeatable Read as an example to demonstrate how MVCC works:

There are two hidden columns for each row: transaction_id and roll_pointer. When transaction A starts, a new Read View with transaction_id=201 is created. Shortly afterward, transaction B starts, and a new Read View with transaction_id=202 is created.

Now transaction A modifies the balance to 200, a new row of the log is created, and the roll_pointer points to the old row. Before transaction A commits, transaction B reads the balance data. Transaction B finds that transaction_id 201 is not committed, it reads the next committed record(transaction_id=200).

Even when transaction A commits, transaction B still reads data based on the Read View created when transaction B starts. So transaction B always reads the data with balance=100.

# Question:

Have you seen isolation levels used in the wrong way? Did it cause serious outages?

# Answer:

Isolation levels being used incorrectly can indeed lead to serious outages in database transactions. When isolation levels are not properly set or managed, it can result in data inconsistencies, concurrency issues, and even data corruption. It is crucial for developers and database administrators to understand and apply the appropriate isolation levels based on the specific requirements of their applications to avoid such problems.

Check out our bestselling system design books:

- Paperback: Amazon
- Digital: ByteByteGo
---
#

# Cloud Computing Services: IaaS, PaaS, SaaS

# Cloud Computing Services: IaaS, PaaS, SaaS

What is IaaS/PaaS/SaaS?

The diagram below illustrates the differences between IaaS (Infrastructure-as-a-Service), PaaS (Platform-as-a-Service), and SaaS (Software-as-a-Service).

Cloud Computing Services: Who Manages What?
Traditional IT
IaaS
PaaS
SaaS

Applications

Data

Runtime

Middleware

OS

Virtualization

Servers

Storage

Networking

You manage
Provider manages
Provider manages
Provider manages

For a non-cloud application, we own and manage all the hardware and software. We say the application is on-premises.

With cloud computing, cloud service vendors provide three kinds of models for us to use: IaaS, PaaS, and SaaS.

IaaS provides us access to cloud vendors' infrastructure, like servers, storage, and networking. We pay for the infrastructure service and install and manage supporting software on it for our application.

PaaS goes further. It provides a platform with a variety of middleware, frameworks, and tools to build our application. We only focus on application development and data.

SaaS enables the application to run in the cloud. We pay a monthly or annual fee to use the SaaS product.

Over to you: which IaaS/PaaS/SaaS products have you used? How do you decide which architecture to use?

Image Source: https://www.ibm.com/cloud/learn/iaas-paas-saas
---
#

# Programming Languages

# Most Popular Programming Languages

Programming languages come and go. Some stand the test of time. Some are shooting stars, while others are rising rapidly on the horizon.

I have drawn a diagram placing the top 38 most commonly used programming languages in one place, sorted by year. Data source: StackOverflow survey.

Year
Programming Languages

1949
Assembly

1958
LISP

1962
Cobol

1972
C

1978
SQL

1980
Objective-C

1984
Matlab

1986
JavaScript

1987
Perl

1989
Bash/Shell

1990
Haskell

1991
Python

1993
PHP

1995
Java

2003
Ruby

2005
Scala

2006
Kotlin

2007
Clojure

2009
Node.js

2010
Swift

2011
Dart

2012
TypeScript

2014
Crystal

# Top 11 Most Commonly Used Programming Languages:

1. JavaScript
2. HTML/CSS
3. Python
4. SQL
5. Java
6. Node.js
7. TypeScript
8. C
9. Bash/Shell
10. C++
11. PHP
---
#
# Programming Languages

# List of Programming Languages

Index
Language

12
C

13
PowerShell

14
Go

15
Kotlin

16
Rust

17
Ruby

18
Dart

19
Assembly

20
Swift

21
R

22
VBA

23
Matlab

24
Groovy

25
Objective-C

26
Scala

27
Perl

28
Haskell

29
Delphi

30
Clojure

31
Elixir

32
LISP

33
Julia

34
F

35
Erlang

36
APL

37
Crystal

38
COBOL

What’s the first programming language you learned? And what are the other languages you learned over the years?
---
#

# Online Payments and Blockchain

# Online Payments and Blockchain

What is the future of online payments?

I don’t know the answer, but I do know one of the candidates is the blockchain.

As a fan of technology, I always seek new solutions to old challenges. A book that explains a lot about an emerging payment system is ‘Mastering Bitcoin’ by Andreas M. Antonopoulos. I want to share my discovery of this book with you because it explains very clearly bitcoin and its underlying blockchain. This book makes me rethink how to renovate payment systems.

|Book Title|Author|
|---|---|
|Mastering Bitcoin|Andreas M. Antonopoulos|

# Takeaways:

1. The bitcoin wallet balance is calculated on the fly, while the traditional wallet balance is stored in the database. You can check chapter 12 of System Design Interview Volume 2, on how to implement a traditional wallet (Link to Book).
---
#

# Payment Solution Recommendation for Elon Musk's Base on Mars

# Payment Solution Recommendation for Elon Musk's Base on Mars

Based on the information provided:

1. What is the golden source of truth for bitcoin?

Answer: The blockchain
2. What defines a set of bytecodes to do basic tasks such as validation for bitcoin and Ethereum?

Answer: The virtual machine
3. If Elon Musk set up a base on planet Mars, what payment solution would you recommend?

Answer: Considering the unique challenges of interplanetary transactions and the need for a secure, decentralized system, I would recommend utilizing a blockchain-based payment solution similar to bitcoin or Ethereum. This would ensure transparency, security, and reliability in financial transactions on Mars.
---
#

# SSO (Single Sign-On)

# What is SSO (Single Sign-On)?

A friend recently went through the irksome experience of being signed out from a number of websites they use daily. This event will be familiar to millions of web users, and it is a tedious process to fix. It can involve trying to remember multiple long-forgotten passwords, or typing in the names of pets from childhood to answer security questions. SSO removes this inconvenience and makes life online better. But how does it work?

Basically, Single Sign-On (SSO) is an authentication scheme. It allows a user to log in to different systems using a single ID.

# Illustration of How SSO Works:

Step
Description

1
A user visits Gmail, or any email service. Gmail finds the user is not logged in and so redirects them to the SSO authentication server, which also finds the user is not logged in. As a result, the user...

2
Requests authentication, creates a token and global session, authenticates with the token, and registers the system (Gmail).

8
Navigates from Gmail to YouTube.

9
Requests authentication.

10
Already logged in, authenticates with token.

12
Registers the system (YouTube).
---
#

# SSO Authentication Process

# SSO Authentication Process

Steps
Description

1
User is redirected to the SSO login page, where they enter their login credentials.

2-3
The SSO authentication server validates the credentials, creates the global session for the user, and creates a token.

4-7
Gmail validates the token in the SSO authentication server. The authentication server registers the Gmail system, and returns "valid." Gmail returns the protected resource to the user.

8
From Gmail, the user navigates to another Google-owned website, for example, YouTube.

9-10
YouTube finds the user is not logged in, and then requests authentication. The SSO authentication server finds the user is already logged in and returns the token.

11-14
YouTube validates the token in the SSO authentication server. The authentication server registers the YouTube system, and returns "valid." YouTube returns the protected resource to the user.

The process is complete and the user gets back access to their account.

# Questions:

1. Question 1: Have you implemented SSO in your projects? What is the most difficult part?
2. Question 2: What's your favorite sign-in method and why?

Check out our bestselling system design books:

Paperback: Amazon

Digital: ByteByteGo
---
#

# Secure Password Storage

# How to store passwords safely in the database?

Let’s take a look.

# Things NOT to do

- Storing passwords in plain text is not a good idea because anyone with internal access can see them.
- Storing password hashes directly is not sufficient because it is prone to precomputation attacks, such as rainbow tables.
- To mitigate precomputation attacks, we salt the passwords.

# What is salt?

According to OWASP guidelines, “a salt is a unique, randomly generated string that is added to each password as part of the hashing process”.
---
#

# Password Storage and Validation

# How to store passwords in DB?

|Provided by client|Randomly generated salt|hash|
|---|---|---|
|password|salt|hash(password + salt)|

A salt is not meant to be secret and it can be stored in plain text in the database. It is used to ensure the hash result is unique to each password.

# How to validate a password?

To validate a password, it can go through the following process:

1. A client enters the password.
2. The system fetches the corresponding salt from the database.
---
#

# Password Safety Mechanisms

# Password Safety Mechanisms

When it comes to ensuring password safety, there are several mechanisms that can be implemented:

|Mechanism|Description|
|---|---|
|1. Password Complexity Requirements|Enforcing the use of strong passwords with a combination of uppercase letters, lowercase letters, numbers, and special characters.|
|2. Multi-Factor Authentication (MFA)|Requiring users to provide additional verification factors such as SMS codes, biometrics, or authenticator apps.|
|3. Password Expiration Policies|Regularly prompting users to change their passwords to reduce the risk of unauthorized access.|
|4. Account Lockout Mechanisms|Temporarily locking out an account after multiple failed login attempts to prevent brute force attacks.|
|5. Password Hashing Algorithms|Using strong and secure hashing algorithms like bcrypt or scrypt to protect stored passwords.|

By implementing these mechanisms, organizations can enhance the security of their password systems and better protect user accounts.
---
#

# HTTPS Encryption and Decryption

# Questions and Answers about HTTPS Encryption and Decryption

# Question 1: How does HTTPS work?

HTTPS is an extension of HTTP that transmits encrypted data using Transport Layer Security (TLS). When data is hijacked online, the hijacker only gets binary code.

# Question 2: How is the data encrypted and decrypted?

|Step|Description|
|---|---|
|Step 1|The client and server establish a TCP connection.|
|Step 2|The client sends a "client hello" to the server with encryption algorithms and TLS version. The server responds with a "server hello" confirming support for algorithms and TLS version.|
---
#

# HTTPS Encryption

# HTTPS Encryption Process

The process of HTTPS encryption involves several steps:

1. The server sends the SSL certificate to the client containing the public key, host name, and expiry dates.
2. The client validates the certificate.
3. After validation, the client generates a session key and encrypts it using the public key.
4. The server decrypts the session key with its private key.
5. Both client and server now use the same session key for symmetric encryption.
6. Encrypted data is transmitted securely in a bi-directional channel.

# Reasons for Switching to Symmetric Encryption

HTTPS switches to symmetric encryption during data transmission due to:

1. Security: Asymmetric encryption is one-way, making it vulnerable to decryption if data is sent back to the client.
2. Server Resources: Asymmetric encryption adds significant mathematical overhead, making it unsuitable for long data transmissions.

# Performance Overhead of HTTPS vs. HTTP

HTTPS adds more performance overhead compared to HTTP due to the encryption processes involved, especially the asymmetric encryption during the initial handshake.

For more information on system design, check out our bestselling books:

- Paperback: Amazon
- Digital: ByteByteGo

Performance overhead: 17
---
#

# Design Patterns Learning

# How to learn design patterns?

Besides reading a lot of well-written code, a good book guides us like a good teacher.

# Recommended Book:

Head First Design Patterns, Second Edition

Authors
Book Title

Erich Gamma
Design Patterns: Elements of Reusable Object-Oriented Software

Richard Helm

John Vlissides

Elisabeth Robson

Eric Freeman

Foreword by Grady Booch

When I began my journey in software engineering, I found it hard to understand the classic textbook, Design Patterns, by the Gang of Four. Luckily, I discovered Head First Design Patterns in the school library. This book solved a lot of puzzles for me. When I went back to the Design Patterns book, everything looked familiar and more understandable.

Last year, I bought the second edition of Head First Design Patterns and read through it. Here are a few things I like about the book:

1. Brain-Friendly Guide
2. Illustrated Volume

Source: O'Reilly
---
#
# Understanding Challenging Topics

# Book Review: Understanding Software Design Patterns

This book tackles the challenge of understanding software's abstract nature by utilizing visualization techniques. It addresses the difficulty in comprehending software architecture and design patterns due to their invisible nature within code and binary files. The book stands out for its use of diagrams, arrows, and comments on almost every page, making complex concepts easier to grasp.

One of the key strengths of this book is its approachability for beginners. It acknowledges the common hesitations and questions that learners may have when delving into a new skill. By presenting design patterns from the student's perspective, the book effectively guides readers through the material by addressing their queries and providing clear explanations.

Personally, I found this book immensely helpful in demystifying challenging topics within software development. The visual aids and student-centric approach made it easier for me to grasp complex concepts and deepen my understanding of software design patterns.

What book has helped you understand a challenging topic? Share your thoughts!
---
#

# Database Selection Guide

# A Visual Guide on How to Choose the Right Database

Picking a database is a long-term commitment so the decision shouldn’t be made lightly. The important thing to keep in mind is to choose the right database for the right job.

Data Type
Use Case
Database Options

Structured
Transactions (OLTP)
RDS Aurora, Azure SQL Database, Cloud Spanner, OracleDB, MySQL, PostgreSQL

Structured
Analytics (OLAP)
RedShift, Azure Synapse, BigQuery, Snowflake, ClickHouse

Dictionary
Key-Value
DynamoDB, Cosmos DB, Big Table, ScyllaDB, Ignite

2-D Key-Value
Cache
ElastiCache, Azure Cache for Redis, Memory store, Memcached, Hazelcast, Ignite

Wide Column
Time Series
Timestream, Cosmos DB, Big Table, InfluxDB, ScyllaDB, OpenTSDB

Data Type
Time Series
Quantum Ledger Database, Azure SQL Database, Hyperledger Fabric

Data Type
Location & Geo-entities
Keyspaces, Cosmos DB, Big Table, BigQuery, PostGIS, MongoDB

Entity-Relationships
Graph
Neptune, Cosmos DB, Big Table, JanusGraph, Neo4J, Giraph

Nested Objects (XML/JSON)
Document
Document DB, Cosmos DB, Firestore, MongoDB, Couchbase, Solr

Unstructured
Full Text Search
OpenSearch, Cognitive Search, APIs on Datastores, Elastic Search, Solr, Elassandra

Unstructured
Blob
Blob Storage, Cloud Storage, HDFS, MinIO

Source: Salish Chandra Gupta

License: CC BY-NC-ND 4.0 International License

For more information, visit Creative Commons

Follow Salish Chandra Gupta on Twitter and LinkedIn
---
#
# Database Workload Question

# Database Workload Question:

Data can be structured (SQL table schema), semi-structured (JSON, XML, etc.), and unstructured (Blob).

Common database categories include:

- Relational
- Columnar
- Key-value
- In-memory
- Wide column
- Time Series
- Immutable ledger
- Geospatial
- Graph
- Document
- Text search
- Blob

Thanks, Satish Chandra Gupta

Over to you - Which database have you used for which workload?

Which database category would you choose for the following workloads:

Workload
Database Category

Storing customer information in a structured format
Relational

Analyzing large volumes of data for business intelligence
Columnar

Storing session data for a web application
Key-value

Real-time data processing and analytics
In-memory

Storing time-series data like stock prices
Time Series

Recording every change made to a dataset
Immutable ledger

Managing geographical data and performing spatial queries
Geospatial

Representing relationships between entities in a network
Graph

Storing and retrieving documents like PDFs or Word files
Document

Enabling full-text search capabilities on a large dataset
Text search

Storing unstructured data like images or videos
Blob
---
#

# Globally Unique IDs

# Do you know how to generate globally unique IDs?

In this post, we will explore common requirements for IDs that are used in social media such as Facebook, Twitter, and LinkedIn.

# Requirements:

|Requirement|Description|
|---|---|
|Globally unique|IDs must be unique globally to avoid collisions.|
|Roughly sorted by time|User IDs, post IDs should be roughly sorted by time without additional info.|
|Numerical values only|IDs should be numerical for natural sorting by time.|
|64 bits|IDs should be 64 bits in size for scalability.|
|Highly scalable, low latency|Ability to generate a large number of IDs per second with low latency is crucial.|

# Unique ID Generator

blog:bytebytego.com

# Common Solutions:

- Distributed ID Generator
- Pros: Easy to generate globally unique IDs.
- Cons: IDs are not sorted.
- UUID
- Pros: Universally unique and sorted.
- Cons: Complex to understand.
- DB ticket server
- Pros: Single server used.
- Cons: IDs are not sorted, multiple servers are used.
- Twitter Snowflake ID
- Pros: Widely used, endorsed by Twitter.
- Cons: Requires understanding, used by Discord/Twitter.
---
#

# Question

# Question:

What kind of ID generators have you used?
---
#

# Twitter Tech Talk Summary

# How does Twitter work?

This post is a summary of a tech talk given by Twitter in 2013. Let’s take a look at the lifecycle of a tweet:

Step
Description

1
A tweet comes in through the Write API.

2
The Write API routes the request to the Fanout service.

3
The Fanout service does a lot of processing and stores them in the Redis cache.
---
#

# System Architecture Overview

# System Architecture Overview

# Timeline Service:

|Step|Description|
|---|---|
|4|The Timeline service is used to find the Redis server that has the home timeline on it.|
|5|A user pulls their home timeline through the Timeline service.|

# Search & Discovery:

- Ingester: annotates and tokenizes Tweets so the data can be indexed.
- Earlybird: stores search index.
- Blender: creates the search and discovery timelines.

# Push Compute:

- HTTP push
- Mobile push

Disclaimer: This article is based on the tech talk given by Twitter in 2013 (source). Even though many years have passed, it’s still quite relevant. I redraw the diagram as the original diagram is difficult to read.

# Over to you:

Do you use Twitter? What are some of the biggest differences between LinkedIn and Twitter that might shape their system architectures?

Check out our bestselling system design books.

Paperback: Amazon

Digital: ByteByteGo

25
---
#

# Process vs Thread

# What is the difference between Process and Thread?

To better understand this question, let’s first take a look at what is a Program. A Program is an executable file containing a set of instructions and passively stored on disk. One program can have multiple processes. For example, the Chrome browser creates a different process for every single tab.

A Process means a program is in execution. When a program is loaded into the memory and becomes active, the program becomes a process. The process requires some essential resources such as registers, program counter, and stack.

|Program|Process|Thread|
|---|---|---|
|Disk|RAM|Thread|
|Instruction|Instruction 2|Instruction #n|
---
#

# Thread, Process, and Coroutine

# Thread, Process, and Coroutine

A Thread is the smallest unit of execution within a process.

The following process explains the relationship between program, process, and thread:

1. The program contains a set of instructions.
2. The program is loaded into memory. It becomes one or more running processes.
3. When a process starts, it is assigned memory and resources. A process can have one or more threads. For example, in the Microsoft Word app, a thread might be responsible for spelling checking and the other thread for inserting text into the doc.

Main differences between process and thread:

- Processes are usually independent, while threads exist as subsets of a process.
- Each process has its own memory space. Threads that belong to the same process share the same memory.
- A process is a heavyweight operation. It takes more time to create and terminate.
- Context switching is more expensive between processes.
- Inter-thread communication is faster for threads.

# Questions:

1. 1). Some programming languages support coroutine. What is the difference between coroutine and thread?
Answer: A coroutine is a component that allows for cooperative multitasking within a single thread. Unlike threads, coroutines are not executed concurrently but rather cooperatively yield control to other coroutines.
2. 2). How to list running processes in Linux?
Answer: In Linux, you can list running processes using the command ps or top. The ps command provides a snapshot of the current processes, while top continuously updates the list of processes.

Check out our bestselling system design books.

Paperback: Amazon Digital: ByteByteGo.

27
---
#

# Interview Question: Design Google Docs

# Interview Question: Design Google Docs

|Client|Client|Client|
|---|---|---|
|WebSocket Server| | |
|Message Queue| | |
|Cache|File Operation Server| |
|File meta|File content|Operations|

1. Clients send document editing operations to the WebSocket Server.
2. The real-time communication is handled by the WebSocket Server.
3. Documents operations are persisted in the Message Queue.

28
---
#

# File Operation Server and Conflict Resolution

# Questions:

1. What are the three types of data stored by the File Operation Server?
2. What are some common algorithms used for real-time conflict resolution?
3. Which algorithm does Google Doc use according to the information provided?
4. Which algorithm is mentioned as an active area of research for real-time concurrent editing?
5. Have you encountered any issues while using Google Docs? If yes, what do you think might have caused the issue?

# Answers:

1. The three types of data stored are file metadata, file content, and operations.
2. Common algorithms for conflict resolution include Operational Transformation (OT), Differential Synchronization (DS), and Conflict-free Replicated Data Type (CRDT).
3. Google Doc uses Operational Transformation (OT) according to the provided information.
4. Conflict-free Replicated Data Type (CRDT) is mentioned as an active area of research for real-time concurrent editing.
5. Personal response required.

Source: Adapted from the File Operation Server and Conflict Resolution text.
---
#

# Deployment Strategies

# Deployment Strategies

Deploying or upgrading services is risky. In this post, we explore risk mitigation strategies.

# Deployment Strategies Diagram

Multi-Service Deployment
Blue-Green Deployment
Canary Deployment
A/B Test

Service Service B V1.0 V1.2 Service C Service V2.0 V3.1 upgrade Service Service B V1.1 V1.3 Service Service D V2.1 V3.1.1
Staging Production Service A Service V1.1 V1.0 Service B Service V1.1 V1.0 upgrade Production Staging Service Service V1.1 V1.0 Service B Service V1.1 V1.0
Service Service V1.0 V1.0 upgrade Service Service V1.1 V1.0 verify Service Service V1.1 V1.1 Service Service V1.1 V1.1
Service Service V1.0 V1.0 upgrade Service Service V1.1 V1.2 V1.1 = 50% V1.2 = 25% Service Service V1.2 V1.0

# Multi-Service Deployment

In this model, we deploy new changes to multiple services simultaneously. This approach is easy to implement. But since all the services are upgraded at the same time, it is hard to manage and test dependencies. It’s also hard to rollback safely.

Reference: 30
---
#

# Deployment Strategies

# Deployment Strategies

# Blue-Green Deployment

With blue-green deployment, we have two identical environments: one is staging (blue) and the other is production (green). The staging environment is one version ahead of production. Once testing is done in the staging environment, user traffic is switched to the staging environment, and the staging becomes the production. This deployment strategy is simple to perform rollback, but having two identical production quality environments could be expensive.

# Canary Deployment

A canary deployment upgrades services gradually, each time to a subset of users. It is cheaper than blue-green deployment and easy to perform rollback. However, since there is no staging environment, we have to test on production. This process is more complicated because we need to monitor the canary while gradually migrating more and more users away from the old version.

# A/B Test

In the A/B test, different versions of services run in production simultaneously. Each version runs an “experiment” for a subset of users. A/B test is a cheap method to test new features in production. We need to control the deployment process in case some features are pushed to users by accident.

# Question:

Which deployment strategy have you used? Did you witness any deployment-related outages in production and why did they happen?

Answer: Please provide your response based on your experience with deployment strategies.
---
#

# Flowchart of How Slack Decides to Send a Notification

# Flowchart of How Slack Decides to Send a Notification

It is a great example of why a simple feature may take much longer to develop than many people think.

When we have a great design, users may not notice the complexity because it feels like the feature is just working as intended.

# Question:

What's your takeaway from this diagram?

|Should send notification?|Use of DnD?|Lezurd|Prcl Uilo|Purgna|
|---|---|---|---|---|
|Tacl|From cnt|Nothing|Everything|Mentions|
|@ clau|Fichiaht Komt|Cenmont|Mentions|Never|
| | |Usipusurcu|Yes|PosiMch|Koie?|

Image source: slack.engineering
---
#

# Amazon Builders' Library

# Amazon Builders' Library

How does Amazon build and operate the software?

In 2019, Amazon released The Amazon Builders' Library. It contains architecture-based articles that describe how Amazon architects, releases, and operates technology.

|Level 400|Level 400|Level 300|
|---|---|---|
|Workload isolation using shuffle-sharding|Architecting and operating resilient serverless|Caching challenges and strategies|
|Author: Colm MacCarthaigh|Author: David Yanacek|Authors: Matt Brinkley; Jas Chhabra|
|Shuffle Sharding is one of our core techniques for drastically limiting the scope of impact of operational issues.|In this video we cover what AWS does to build reliable and resilient services, including avoiding modes and overload, performing bounded work, throttling at multiple layers, guarding concurrency.|Improving latency and availability with caching while avoiding the modal behavior they can introduce.|
|PDF Kindle|ARCHITECTURE|PDF Kindle|

|Level 300|Level 400|Level 400|
|---|---|---|
|Amazon's approach to security during development|Avoiding insurmountable queue backlogs|Implementing health checks|
|Author: Colm MacCarthaigh|Author: David Yanacek|Author: David Yanacek|
|In this video, learn about how AWS prioritizes draining important security during development.|Prioritizing draining important queue backlogs.|Automatically detecting and mitigating.|

As of today, it has published 26 articles. It took me two weekends to go through all the articles. I’ve had great fun and learned a lot. Here are some of my favorites:

- Making retries safe with idempotent APIs
- Timeouts, retries, and backoff with jitter
- Beyond five 9s: Lessons from our highest available data planes
- Caching challenges and strategies
- Ensuring rollback safety during deployments
- Going faster with continuous delivery
---
#
# System Design and Design Principles

# Challenges with Distributed Systems:

Discuss the challenges associated with distributed systems.

# Amazon's Approach to High-Availability Deployment:

Explain Amazon's approach to high-availability deployment.

# Favorite Place to Learn System Design and Design Principles:

Where do you prefer to learn about system design and design principles?

Link to The Amazon Builders' Library: aws.amazon.com/builders-library
---
#

# Secure Web API Access Design

# How to design a secure web API access for your website?

When we open web API access to users, we need to make sure each API call is authenticated. This means the user must be who they claim to be.

In this post, we explore two common ways:

1. Token based authentication
2. HMAC (Hash-based Message Authentication Code) authentication

The diagram below illustrates how they work:

35
---
#
# Token based authentication

# Token based authentication

Step 1 - the user enters their password into the client, and the client sends the password to the Authentication Server.

Step
Description

1
The user enters their password into the client, and the client sends the password to the Authentication Server.

2
Authentication Server receives the password and generates a token.

3
Client sends a request with the token to the Web Server.

4
Web Server authenticates the token and provides access to the requested resource.

5
Client generates HMAC signature on the client side.

6
Web Server generates HMAC signature on the server side and compares it with the client's HMAC signature.
---
#

# Authentication Mechanisms

# Authentication Mechanisms

Step 2 - the Authentication Server authenticates the credentials and generates a token with an expiry time.

Steps 3 and 4 - now the client can send requests to access server resources with the token in the HTTP header. This access is valid until the token expires.

HTTP based

This mechanism generates a Message Authentication Code (signature) by using a hash function (SHA256 or MD5).

Steps 1 and 2 - the server generates two keys, one is Public APP ID (public key) and the other one is API Key (private key).

Step 3 - we now generate a HMAC signature on the client side (hmac A). This signature is generated with a set of attributes listed in the diagram.

Step 4 - the client sends requests to access server resources with hmac A in the HTTP header.

Step 5 - the server receives the request which contains the request data and the authentication header. It extracts the necessary attributes from the request and uses the API key that’s stored on the server side to generate a signature (hmac B).

Steps 6 and 7 - the server compares hmac A (generated on the client side) and hmac B (generated on the server side). If they are matched, the requested resource will be returned to the client.

Question: How does HMAC authentication ensure data integrity? Why do we include “request timestamp” in HMAC signature generation?

—

Check out our bestselling system design books.

Paperback: Amazon Digital: ByteByteGo.
---
#

# Microservices Collaboration

# Microservices Collaboration

How do microservices collaborate and interact with each other?

There are two ways: Orchestration and Choreography.

Collaboration Type
Description

Orchestration
The orchestrator acts as a center of authority, responsible for invoking and combining the services.

Choreography
Describes the exchange of messages and rules by which microservices interact, similar to dancers following a choreographer's rules.

The diagram below illustrates the collaboration of microservices:

Orchestration
Choreography

Service A Service B invoke reply reply invoke Orchestrator invoke reply Service C Service D
Service A Service B invoke reply reply invoke Service C Service D

Key points:

- Orchestration: Services are more loosely coupled, domain boundaries are clearly defined, and test cases can be confined in the domains.
- Choreography: Service dependency is complicated, making debugging and testing more difficult, point-to-point communications, and fault tolerance scenarios are complex.

Service choreography describes the exchange of messages and rules by which microservices interact, while orchestration involves an orchestrator invoking and combining services.
---
#

# Orchestration in Microservices

# Orchestration in Microservices

The orchestration pattern in microservices describes the interactions between all the participating services. It acts as a conductor leading the services, similar to a musical symphony. The orchestration pattern also manages transactions among different services.

# The benefits of orchestration:

1. Reliability: Orchestration provides built-in transaction management and error handling, making it more reliable compared to choreography.
2. Scalability: Adding a new service in orchestration only requires modifying the orchestrator's rules, simplifying scalability compared to choreography where all interacting services need modification.

# Limitations of orchestration:

1. Performance: Centralized orchestration can lead to higher latency compared to choreography, and throughput is limited by the orchestrator's capacity.
2. Single point of failure: If the orchestrator fails, services cannot communicate. High availability measures are necessary to mitigate this risk.

# Real-world use case:

Netflix Conductor is a microservice orchestrator that demonstrates the practical application of orchestration in managing microservices. For more details on the orchestrator design, refer to Netflix's resources.

# Question:

Have you used orchestrator products in production? What are their pros & cons?

— Check out our bestselling system design books. Paperback: Amazon Digital: ByteByteGo.

39
---
#

# Virtualization vs Containerization

# Virtualization vs Containerization

The diagram below illustrates the layered architecture of virtualization and containerization:

Bare Metal
Virtualized
Containerized
Containerized on Virtualized

Operating System
Host Operating System
Host Operating System
Host Operating System
Host Operating System

Virtual Machine
App1 App2
App1 App2
ContainerEngine
ContainerEngine

Container

Container
Container

"Virtualization is a technology that allows you to create multiple simulated environments or dedicated resources from a single, physical hardware system" [1].

"Containerization is the packaging together of software code with all its necessary components like libraries, frameworks, and other dependencies so that they are isolated in their own 'container'" [2].

# The major differences are:

- In virtualization, the hypervisor creates an abstraction layer over hardware, so that multiple operating systems can run alongside each other. This technique is considered to be the first generation of cloud computing.
- Containerization is considered to be a lightweight version of virtualization, which virtualizes the operating system instead of hardware. Without the hypervisor, the containers enjoy faster resource provisioning. All the resources (including code, dependencies) that are...
---
#

# Question

# Question:

How much performance differences have you observed in production between virtualization, containerization, and bare-metal?

# Image Source:

https://lnkd.in/gaPYcGTz

# Sources:

1. Understanding virtualization
2. What is containerization?

41
---
#

# Big Data Cloud Providers Comparison

# Big Data Cloud Providers Comparison

Which cloud provider should be used when building a big data solution?

Cloud Provider
Services

AWS
IoT, Lambda, Glue, Kinesis, RedShift, RDS, Athena, EMR, SageMaker, DynamoDB, QuickSight

Microsoft Azure
IoT Hub, Function, Data Lake Store, Databricks, Cosmos DB, Azure ML, Azure SQL, Event Hub

Google Cloud
Cloud IoT, Cloud Storage, Cloud Function, DataPrep, DataFlow, AutoML, BigQuery, Cloud SQL, Datastore, Bigtable, Memory-store, PubSub

Reference: scgupta linklbig-data-pipeline
---
#

# Common Parts of Solutions

# The common parts of the solutions:

1. Data ingestion of structured or unstructured data.
2. Raw data storage.
3. Data processing, including filtering, transformation, normalization, etc.
4. Data warehouse, including key-value storage, relational database, OLAP database, etc.
5. Presentation layer wip dashboards and real-time notifications.

It is interesting to see different cloud vendors have different names for the same type of products.

For example, the first step and the last step both use the serverless product. The product is called “lambda” in AWS, and “function” in Azure and Google Cloud.

# Question:

Which products have you used in production? What kind of application did you use it for?

Source: S.C. Gupta’s post
---
#

# Question and Answer

# Question:

How to avoid crawling duplicate URLs at Google scale?

# Options:

|Option 1|Use a Set data structure to check if a URL already exists or not. Set is fast, but it is not space-efficient.|
|---|---|
|Option 2|Store URLs in a database and check if a new URL is in the database. This can work but the load to the database will be very high.|
|Option 3|Bloom filter. This option is preferred. Bloom filter was proposed by Burton Howard Bloom in 1970. It is a probabilistic data structure that is used to test whether an element is a member of a set.|

# Explanation of Bloom Filter:

🔹 false: the element is definitely not in the set.

🔹 true: the element is probably in the set.

False-positive matches are possible, but false negatives are not.

The diagram below illustrates how the Bloom filter works. The basic data structure for the Bloom filter is Bit Vector. Each bit represents a hashed value.

Diagram can be inserted here.
---
#

# Bloom Filter Hash Function

# Hash Function in Bloom Filter

Below is the description of how hash functions are used in a Bloom Filter:

Step
Description

Step 1
To add an element to the bloom filter, we feed it to 3 different hash functions (A, B, and C) and set the bits at the resulting positions. Note that both “www.myweb1.com” and “www.myweb2.com” mark the same bit with 1 at index 5. False positives are possible because a bit might be set by another element.

Step 2
When testing the existence of a URL string, the same hash functions A, B, and C are applied to the URL string. If all three bits are set by the hash functions, the URL string is considered to exist in the Bloom Filter.
---
#

# OCR Text Analysis

# OCR Text Analysis

1. What is the significance of the bits in determining the existence of a URL in the dataset?

Answer: If all bits are 1, the URL may exist in the dataset; if any bit is 0, the URL definitely does not exist in the dataset.

2. Why are hash function choices important in the context of URL existence determination?

Answer: Hash functions must be uniformly distributed and fast to ensure efficient processing. For example, RedisBloom and Apache Spark use murmur, while InfluxDB uses xxhash.

3. In the example provided, three hash functions were used. How many hash functions should be used in reality and what are the trade-offs?

Answer: In reality, the number of hash functions used depends on the specific requirements of the system. Using more hash functions can improve accuracy but may also increase computational overhead and memory usage.

4. What hash functions are commonly used by RedisBloom, Apache Spark, and InfluxDB for URL processing?

Answer: RedisBloom and Apache Spark use murmur, while InfluxDB uses xxhash for URL processing.

5. What are some of the bestselling system design books recommended?

Answer: Paperback: Amazon Digital: ByteByteGo.

6. What is the page number mentioned in the OCR text?

Answer: 46
---
#

# SSD Architecture

# SSD Architecture

Why is a solid-state drive (SSD) fast?

“A solid state drive reads up to 10 times faster and writes up to 20 times faster than a hard disk drive.”

“An SSD is a flash-memory based data storage device. Bits are stored into cells, which are made of floating-gate transistors. SSDs are made entirely of electronic components, there are no moving or mechanical parts like in hard drives (HDD)”

SSD Architecture Diagram

SSD Architecture
RAM buffer
Flash        Flash
SSD Controller                 memory      memory
package #0  package
Host                       Processor                                 Channel =0
connection  Host
Interface                               Flash                Channel #1
Logic               Buffer           controller
manager                             Flash       Flash
memory      memory
package #2  package #3
Mapping of Logical and Physical Pages
OS LBA Space                        Physical NAND Flash Pages
Processor SSD
Flexible Logical to Physical Mapping
---
#

# SSD vs HDD

# SSD vs HDD

Based on the information provided:

SSD
HDD

SSD controller operates multiple FLASH particles in parallel
HDD has a single head and can only read from one head at a time

SSD can write multiple pages in parallel
HDD can only read from one head at a time

SSD uses mapping to locate data for faster access
HDD does not have such mapping capabilities

If you are interested in learning more about SSD architecture, you can refer to the resource: Coding for SSDs.

Sources:

1. SSD or HDD: Which Is Right for You?
2. Coding for SSDs
3. Overview of SSD Structure and Basic Working Principle
---
#

# Handling a large-scale outage

# Handling a large-scale outage

This is a true story about handling a large-scale outage written by Staff Engineers at Discord Sahn Lam.

About 10 years ago, I witnessed the most impactful UI bugs in my career.

It was 9PM on a Friday. I was on the team responsible for one of the largest social games at the time. It had about 30 million DAU. I just so happened to glance at the operational dashboard before shutting down for the night.

Every line on the dashboard was at zero.

At that very moment, I got a phone call from my boss. He said the entire game was down. Firefighting mode. Full on.

Everything had shut down. Every single instance on AWS was terminated. HA proxy instances, PHP web servers, MySQL databases, Memcache nodes, everything.

It took 50 people 10 hours to bring everything back up. It was quite a feat. That in itself is a story for another day.

We used a cloud management software vendor to manage our AWS deployment. This was before Infrastructure as Code was a thing. There was no Terraform. It was so early in cloud computing and we were so big that AWS required an advanced warning before we scaled up.

What had gone wrong? The software vendor had introduced a bug that week in their confirmation dialog flow. When terminating a subset of nodes in the UI, it would correctly show in the confirmation dialog box the list of nodes to be terminated, but under the hood, it terminated everything.

Shortly before 9PM that fateful evening, one of our poor SREs fulfilled our routine request and terminated an unused Memcache pool. I could only imagine the horror and the phone conversation that ensured.
---
#
# Software Bugs

# Question:

What kind of code structure could allow this disastrous bug to slip through? We could only guess. We never received a full explanation.

# Question:

What are some of the most impactful software bugs you encountered in your career?
---
#

# AWS Lambda behind the scenes

# AWS Lambda behind the scenes

Serverless is one of the hottest topics in cloud services. How does AWS Lambda work behind the scenes?

Lambda is a serverless computing service provided by Amazon Web Services (AWS), which runs functions in response to events.

# Firecracker MicroVM

Firecracker is the engine powering all of the Lambda functions. It is a virtualization technology developed at Amazon and written in Rust.

|KVM on Bare Metal EC2|Firecracker Microvm|Firecracker Microvm|Customer A's Function|
|---|---|---|---|
|MicroVM Kernel|MicroVM Kernel|Customer B's Function|Managed by AWS Lambda Faaadar|
|Lambda Sandbox Execution Environment|Lambda Sandbox Execution Environment| | |
|Customer A Function Code and Layer Code|Customer A Function Code and Layer Code|Customer B Function Code and Layer Code| |
|Runtime Language|Runtime Language| | |
|Invoke()|Init()| | |

The diagram above illustrates the isolation model for AWS Lambda Workers.
---
#

# AWS Lambda Functions

# Questions and Answers about AWS Lambda Functions

# How are lambdas initiated and invoked?

There are two ways:

1. Synchronous execution:
1. Step 1: The Worker Manager communicates with a Placement Service to provision the sandbox.
2. Step 2: The Worker Manager initializes the function by downloading the Lambda package from S3 and setting up the Lambda runtime.
3. Step 3: The Frontend Worker calls Invoke.
2. Asynchronous execution:
1. Step 1: The Application Load Balancer forwards the invocation to an available Frontend which places the event onto an internal queue (SQS).
2. Step 2: Pollers assigned to the internal queue move the event onto a Frontend synchronously for further processing.

# Question:

Can you think of any use cases for AWS Lambda?

# Sources:

- AWS Lambda whitepaper
- Behind the scenes, Lambda

Image source: [1] [2]
---
#

# HTTP Generations and Problems Solved

# HTTP Generations and Problems Solved

What problem does each generation of HTTP solve?

1. HTTP 1.0: Every request to the same server requires a separate TCP connection.
2. HTTP 1.1: Allows for persistent connections, but doesn't solve the HOL blocking issue.
3. HTTP 2.0: Introduces multiplexing, header compression, and prioritization to address performance issues.
4. HTTP 3.0 (QUIC): Uses UDP instead of TCP, improving speed and security.

# Key Features Illustration

Feature
Description

Keep-Alive
Allows reuse of the same TCP connection.

HTTP "streams" based on UDP
Utilizes UDP for improved performance.

Compressed headers
Reduces overhead by compressing headers.

Multi-class Citizens
Improves prioritization and handling of different types of requests.

HOL blocking occurs when the number of allowed parallel requests in the browser is exceeded, causing subsequent requests to wait for the former ones to complete.
---
#

# HTTP 2.0 and HTTP 3.0 Comparison

# HTTP 2.0 and HTTP 3.0 Comparison

HTTP Version
Year Published
Key Features

HTTP 2.0
2015
- Addresses HOL issue through request multiplexing
- Introduces HTTP streams for multiplexing different exchanges
- Eliminates HOL blocking at the application layer
- HOL still exists at the transport (TCP) layer

HTTP 3.0
First draft published in 2020
- Proposed successor to HTTP 2.0
- Uses QUIC instead of TCP for transport protocol
- Removes HOL blocking in the transport layer
- QUIC based on UDP
- Introduces streams as first-class citizens at the transport layer
- QUIC streams share the same connection
- No additional handshakes or slow starts required for new streams
- Packet loss affecting one stream doesn't affect others

# Upgrade to HTTP 3.0

It is recommended to upgrade to HTTP 3.0 when looking to benefit from improved performance and reduced latency compared to HTTP 2.0. The use of QUIC instead of TCP for the transport protocol in HTTP 3.0 eliminates HOL blocking at the transport layer, providing a more efficient communication mechanism.

# Pros and Cons of HTTP 3.0

# Pros:

- Improved performance and reduced latency
- Elimination of HOL blocking at the transport layer
- Efficient use of QUIC for transport protocol
- Stream independence to prevent packet loss affecting other streams

# Cons:

- Being a newer protocol, compatibility and support may be limited initially
- Potential challenges in transitioning existing systems to HTTP 3.0
---
#

# Scaling a Website to Support Millions of Users

# How to scale a website to support millions of users?

We will explain this step-by-step.

# Evolution of a Simplified eCommerce Website:

The diagram below illustrates the evolution of a simplified eCommerce website. It goes from a monolithic design on one single server, to a service-oriented/microservice architecture.

|Stage|Description|
|---|---|
|Monolithic Design|Initially, the website is designed as a monolith on a single server. This setup works well for small-scale operations but may struggle to handle millions of users.|
|Service-Oriented/Microservice Architecture|To scale the website, it transitions to a service-oriented or microservice architecture. This approach involves breaking down the application into smaller, independent services that can be distributed across multiple servers. This allows for better scalability and performance.|
---
#
# Inventory and User Services

# Inventory and User Services

Inventory Service
User Service

Split services and Database
Load Balancer

Inventory Table
Inventory Table

Inventory Service
User Service

Separate DB workload
Load Balancer

Inventory Service
User Service

Horizontal partitioning
Add cache

Product Cache
Login Cache
---
#

# System Architecture Evolution for Services

# System Architecture Evolution for Services

Suppose we have two services: inventory service (handles product descriptions and inventory management) and user service (handles user information, registration, login, etc.).

1. Step 1 - With the growth of the user base, one single application server cannot handle the traffic anymore. We put the application server and the database server into two separate servers.
2. Step 2 - The business continues to grow, and a single application server is no longer enough. So we deploy a cluster of application servers.
3. Step 3 - Now the incoming requests have to be routed to multiple application servers, how can we ensure each application server gets an even load? The load balancer handles this nicely.
4. Step 4 - With the business continuing to grow, the database might become the bottleneck. To mitigate this, we separate reads and writes in a way that frequent read queries go to read replicas. With this setup, the throughput for the database writes can be greatly increased.
5. Step 5 - Suppose the business continues to grow. One single database cannot handle the load on both the inventory table and user table. We have a few options:

Vertical partition. Adding more power (CPU, RAM, etc.) to the database server. It has a hard limit.
6. Horizontal partition by adding more database servers.
7. Adding a caching layer to offload read requests.

Step 6 - Now we can modularize the functions into different services. The architecture becomes service-oriented / microservice.

# Question:

What else do we need to support an e-commerce website at Amazon’s scale?
---
#

# DevOps Books

# DevOps Books

Book Title
Author
Description

Accelerate
O'Reilly
Presents both the findings and the science behind measuring software delivery performance.

Continuous Delivery
O'Reilly
Introduces automated architecture management and data migration. It also points out key problems and optimal solutions in each area.

Site Reliability Engineering
Google SRE
Famous Google SRE book. Explains the whole life cycle of Google’s development, deployment, and monitoring, and how to manage the world’s biggest software systems.

Effective DevOps
Nicola Forsteren; PhD, Jez Humble
Provides effective ways to improve team coordination.
---
#

# Dev-Ops Books

# Dev-Ops Books Recommendations

|Book Title|Description|
|---|---|
|The Phoenix Project|A classic novel about effectiveness and communications. IT work is compared to manufacturing plant work, emphasizing the need for establishing a system to streamline the workflow. A very interesting read!|
|The DevOps Handbook|Introduces product development, quality assurance, IT operations, and information security in the context of DevOps practices.|

What's your favorite Dev-Ops book?
---
#

# Question and Answer

# Question:

Why is Kafka fast?

# Answer:

Kafka achieves low latency message delivery through Sequential I/O and Zero Copy Principle. The same techniques are commonly used in many other messaging/streaming platforms.

# Diagram:

Producer
Consumer
Explanation

1. Producer writes data to RAM 1.2 Writes to OS Buffer 1.3 Sync to disk periodically
2.1 Loads data from disk 2.2 Directly copies data 2.3 Sends to consumer
Zero Copy Principle illustrated
---
#

# Zero Copy Data Reading Process

# Zero Copy Data Reading Process

Step
Description

Step 2
Consumer reads data without zero-copy

2.1
The data is loaded from disk to OS cache

2.2
The data is copied from OS cache to Kafka application

2.3
Kafka application copies the data into the socket buffer

2.4
The data is copied from socket buffer to network card

2.5
The network card sends data out to the consumer

Step 3
Consumer reads data with zero-copy

3.1
The data is loaded from disk to OS cache

3.2
OS cache directly copies the data to the network card via sendfile() command

3.3
The network card sends data out to the consumer

Zero copy is a shortcut to save the multiple data copies between application context and kernel context. This approach brings down the time by approximately 65%.

Check out our bestselling system design books.

Paperback: Amazon Digital: ByteByteGo.
---
#

# API Styles Comparison

# API Styles Comparison: SOAP vs REST vs GraphQL vs RPC

The diagram below illustrates the API timeline and API styles comparison:

SOAP
REST
GraphQL
RPC

Organized in terms
Simple Object Access Protocol
REpresentational State Transfer
GraphQl
Remote Procedure Call

Format

Learning curve

Community

Use cases

Over time, different API architectural styles are released. Each of them has its own patterns of standardizing data exchange.

You can check out the use cases of each style in the diagram.

Source: AltexSoft

Credit goes to AltexSoft.

Check out our bestselling system design books:

- Paperback: Amazon
- Digital: ByteByteGo

62
---
### Questions:

1. What is the purpose of the Renderer Process in modern browsers?

2. What is the role of the Main thread in modern browsers?

3. How is the DOM Tree related to the rendering process in browsers?

4. What type of content can be found in the Network section of a browser?

5. What is the significance of the Request section in a browser's operation?

### Answers:

1. The Renderer Process in modern browsers is responsible for rendering the HTML document.

2. The Main thread in modern browsers handles tasks such as parsing HTML, executing JavaScript, and updating the DOM.

3. The DOM Tree represents the structure of the HTML document and is crucial for rendering content on the browser.

4. The Network section of a browser contains information about network requests made by the browser to load resources like images, scripts, and stylesheets.

5. The Request section in a browser is where requests for external resources like scripts are initiated, impacting the loading and functionality of web pages.
---
#

# Redis vs Memcached

# Redis vs Memcached

The diagram below illustrates the key differences:

Feature
Memcached
Redis

Data Structure
Key-Value
Key-Value, Hash, Sorted Set

Architecture
Simple
Versatile

Transaction
No
Yes

Snapshots/Persistence
No
RDB, AOF

Pub-sub Messaging
No
Supported

Geospatial Support
No
Supported

Server-side Scripts
No
Supported

Supported Cache Eviction
No
Supported

Replication
No
Supported

# Advantages of Redis Data Structures:

- Recording the number of clicks and comments for each post (hash)
- Sorting the commented user list and deduping the users (zset)
- Caching user behavior history and filtering malicious behaviors (zset, hash)
- Storing boolean information of extremely large data into small space. For example, login status, membership status (bitmap)
---
#

# Optimistic Locking

# Optimistic Locking

Optimistic locking, also referred to as optimistic concurrency control, allows multiple concurrent users to attempt to update the same resource.

There are two common ways to implement optimistic locking: version number and timestamp. Version number is generally considered to be a better option because the server clock can be inaccurate over time. We explain how optimistic locking works with version number.

# How Optimistic Locking Works with Version Number:

The diagram below shows a successful case and a failure case:

|Read v1|Write v2|Read v2|Write v3|
|---|---|---|---|
|User 1|User 1|User 2|User 1|
| | | |Conflict|
| |User 2|Conflict| |
|No conflict| | | |

1. A new column called “version” is added to the database table.
2. Before a user modifies a database row, the application reads the version number of the row.
3. When the user updates the row, the application increases the version number by 1 and writes it back to the database.
4. A database validation check is put in place; the next version number should exceed the current version number by 1. The transaction aborts if the validation fails and the user tries again from step 2.
---
#

# Race Conditions Solutions

# Race Conditions Solutions

Optimistic locking is usually faster than pessimistic locking because we do not lock the database. However, the performance of optimistic locking drops dramatically when concurrency is high.

To understand why, consider the case when many clients try to reserve a hotel room at the same time. Because there is no limit on how many clients can read the available room count, all of them read back the same available room count and the current version number. When different clients make reservations and write back the results to the database, only one of them will succeed, and the rest of the clients receive a version check failure message. These clients have to retry. In the subsequent round of retries, there is only one successful client again, and the rest have to retry. Although the end result is correct, repeated retries cause a very unpleasant user experience.

# Question:

What are the possible ways of solving race conditions?

Possible Solutions
1. Use synchronization mechanisms like locks to control access to shared resources.
2. Implement atomic operations to ensure pat critical sections are executed wipout interruption.
3. Utilize transaction management to maintain data consistency and isolation levels.
4. Employ version control techniques to track changes and resolve conflicts efficiently.
---
#

# Tradeoff between Latency and Consistency

# Tradeoff between Latency and Consistency

Understanding the tradeoffs is crucial in system design interviews and real-world system design. When it comes to data replication, there exists a fundamental tradeoff between latency and consistency, as depicted in the diagram below:

|API service wait time|Data routing service|Primary data node|Secondary data node|Option|
|---|---|---|---|---|
|First option: Best consistency Highest latency|Secondary data node 2|Data routing service|Secondary data node|Data is considered as successfully saved after all three nodes store the data|
|Secondary data node 2| | | | |
|Secondary data node| | | | |
|Second option: Medium consistency Medium latency|Secondary data node 2|Data routing service|Secondary data node|Data is considered as successfully saved after the primary and one of the secondaries store the data|
|Secondary data node 2| | | | |
|Secondary data node| | | | |
|Third option: Worst consistency Lowest latency|Secondary data node 2|Data routing service|Secondary data node|Data is considered as successfully saved after the primary persists the data|
|Secondary data node 2| | | | |
|Secondary data node| | | | |

Both the second and third options represent forms of eventual consistency.

Data is considered as successfully saved after all three nodes store the data: This approach has the best consistency but the highest latency.

Data is considered as successfully saved after the primary and one of the secondaries store the data: This approach has medium consistency and medium latency.

Data is considered as successfully saved after the primary persists the data: This approach has the worst consistency but the lowest latency.

Figure 9.11: Trade-off between consistency and latency
---
#

# Cache Miss Attack

# Cache Miss Attack

Caching is awesome but it doesn’t come without a cost, just like many things in life.

One of the issues is Cache Miss Attack. It refers to the scenario where data to fetch doesn't exist in the database and the data isn’t cached either. So every request hits the database eventually, defeating the purpose of using a cache. If a malicious user initiates lots of queries with such keys, the database can easily be overloaded.

The diagram below illustrates the process:

read cache
read db
read k3
read dbl

cache miss
no data
cache miss
no data

write k3-null

read found

not found

Two approaches are commonly used to solve this problem:

1. Approach 1
2. Approach 2
---
#

# System Design Tips

# System Design Tips

# 1. How can you handle cache keys wip null value effectively?

Set a short TTL (Time to Live) for keys wip null value.

# 2. What is pe use of a Bloom filter in system design?

A Bloom filter is a data structure pat can rapidly tell us wheper an element is present in a set or not. It helps in checking if a key exists in pe cache or database.

# 3. How does using a Bloom filter impact pe cache and database layers?

If pe key exists, pe request first goes to pe cache and pen queries pe database if needed. If pe key doesn't exist in pe data set, pe query will not hit pe cache or database layer.

Check out our bestselling system design books:

- Paperback: Amazon
- Digital: ByteByteGo
---
#

# Linux Performance Observability Tools

# Linux Performance Observability Tools

How to diagnose a mysterious process that’s taking too much CPU, memory, IO, etc?

The diagram below illustrates helpful tools in a Linux system:

Tool
Description

strace
Trace system calls and signals

ltrace
Library call tracer

snstat
Network statistics

sar
System activity reporter

opensnoop
Trace file opens

lsof
List open files

fatrace
File access trace

filelife
File lifetime trace

perf
Performance analysis tools

Ftrace
Function tracer

LTTng
Linux Trace Toolkit Next Generation

BCC
BPF Compiler Collection

bpftrace
BPF tracing tool

ext4dist
Ext4 filesystem distribution

ext4slower
Ext4 slow operations

iostat
Input/output statistics

biosnoop
BIOS I/O operations snooper

blktrace
Block layer IO tracer

vmstat
Virtual memory statistics

pidstat
Process statistics

top
Display and update sorted information about processes

atop
Advanced interactive monitor

netstat
Network statistics

Additional tools:

- vmstat - reports information about processes, memory, paging, block IO, traps, and CPU activity.
- iostat - reports CPU and input/output statistics of the system.
- netstat - displays statistical data related to IP, TCP, UDP, and ICMP protocols.
- lsof - lists open files of the current system.
- pidstat - monitors the utilization of system resources by all or specified processes, including CPU, memory, device IO, task switching, threads, etc.
---
#

# Cache Strategies

# Cache Strategies

What are the top cache strategies?

- Read data from the system:
- Cache aside
- Read through
- Write data to the system:
- Write around
- Write back
- Write through

The diagram below illustrates how those 5 strategies work. Some of the caching strategies can be used together.

Diagram:
---
#

# Caching Strategies

# Caching Strategies

Strategy
Read Strategy
Write Strategy

Cache Aside
- 1. Read
- 2. Cache
- 3. Read DB
- 4. Get Data
- 5. Update Cache

- 1. Write DB
- 2. Read from Cache (if data exists)
- 3.1 Read from DB (if data does not exist)
- 3.2 Update Cache

Read Through
- 1. Read
- 2. Cache
- 3. Read
- 4. Get Data
- 5. Update Cache

- Write Strategy
- Write Back

Write Around
- Application

- 1. Write DB
- 2. Write to Cache
- 3. Write to DB once in awhile

Write Through
- Application

- 1. Write to Cache
- 2. Write to DB immediately

I left out a lot of details as that will make the post very long. Feel free to leave a comment so we can learn from each other.

72
---
#

# Caching Strategies

# Caching Strategies

Question: What are the pros and cons of each caching strategy? How to choose the right one to use?

|Strategy|Pros|Cons|
|---|---|---|
|Write-Through|Ensures data consistency in cache and database|Slower write operations due to synchronous database writes|
|Write-Around|Reduces the burden on the cache for infrequently accessed data|Data not available in cache for subsequent reads|
|Write-Back|Improves write performance by buffering writes in cache|Potential data loss in case of cache failure|

To choose the right caching strategy, consider factors like data access patterns, system requirements, and trade-offs between performance and data consistency.

For more in-depth information on system design, check out our bestselling books:

- Paperback: Amazon
- Digital: ByteByteGo

Page: 73
---
#

# Optimizing Performance for Large File Uploads to S3

# Optimizing Performance for Large File Uploads to S3

How can we optimize performance when we upload large files to object storage service such as S3?

Before we answer this question, let's take a look at why we need to optimize this process. Some files might be larger than a few GBs. It is possible to upload such a large object file directly, but it could take a long time. If the network connection fails in the middle of the upload, we have to start over. A better solution is to slice a large object into smaller parts and upload them independently. After all the parts are uploaded, the object store re-assembles the object from the parts. This process is called multipart upload.

The diagram below illustrates how multipart upload works:

Multipart Upload
Data Store

Multipart upload initiation
uploadID

Part 1
uploadID ETag

Part 2
uploadID ETag

Part 8
uploadID ETag

Multipart upload completion
Success
---
#

# Multipart Upload Process

# Multipart Upload Process

Step
Description

1
The client calls the object storage to initiate a multipart upload.

2
The data store returns an uploadID, which uniquely identifies the upload.

3
The client splits the large file into small objects and starts uploading. Let’s assume the size of the file is 1.6GB and the client splits it into 8 parts, so each part is 200 MB in size. The client uploads the first part to the data store together with the uploadID it received in step 2.

4
When a part is uploaded, the data store returns an ETag, which is essentially the md5 checksum of that part. It is used to verify multipart uploads.

5
After all parts are uploaded, the client sends a complete multipart upload request, which includes the uploadID, part numbers, and ETags.

6
The data store reassembles the object from its parts based on the part number. Since the object is really large, this process may take a few minutes. After reassembly is complete, it returns a success message to the client.

Check out our bestselling system design books.

Paperback: Amazon Digital: ByteByteGo.

75
---
#

# Redis Speed Reasons

# Why is Redis so Fast?

There are 3 main reasons as shown in the diagram below:

Register
L1 Cache
Socket1
Socket2

L2 Cache
Socket3
Task
Event

L3 Cache
Socket1

Event

RAM

Socket3
Processors

SSD

HDD

1. Redis is a RAM-based database. RAM access is at least 1000 times faster than random disk access.

2. Redis leverages IO multiplexing and single-threaded execution loop for execution efficiency.

3. Redis leverages several efficient lower-level data structures.

# Question:

Another popular in-memory store is Memcached. Do you know the differences between Redis and Memcached?

You might have noticed the style of this diagram is different from my previous posts. Please let me know which one you prefer.

Check out our bestselling system design books.

Paperback: Amazon Digital: ByteByteGo.
---
#

# SWIFT Payment Network

# SWIFT Payment Network

You probably heard about SWIFT. What is SWIFT? What role does it play in cross-border payments? You can find answers to those questions in this post.

# SWIFT for Cross-Border Payments

SWIFT, the Society for Worldwide Interbank Financial Telecommunication, is the main secure messaging system that links the world's banks. It is Belgium-based and run by its member banks, handling millions of payment messages per day.

# Diagram: Payment Message Transmission

|Bank A (New York)|Regional Processor A (New York)|Regional Processor B (London)|Bank B (London)|
|---|---|---|---|
|Send message with transfer details|Receive message|Send report|Receive message|
| |Validate message|Authorize Regional Processor| |
| |Store the message temporarily|Send message to Bank B| |
| |Send ACK/NAK to Bank A| | |
---
#
# Message Processing Workflow

# Message Processing Workflow

Step
Description

Step 2
Regional processor validates the format and sends it to Slice Processor A. The Regional Processor is responsible for input message validation and output message queuing. The Slice Processor is responsible for storing and routing messages safely.

Step 3
Slice Processor A stores the message.

Step 4
Slice Processor A informs Regional Processor A the message is stored.

Step 5
Regional Processor A sends ACK/NAK to Bank A. ACK means a message will be sent to Bank B. NAK means the message will NOT be sent to Bank B.

Step 6
Slice Processor A sends the message to Regional Processor B in London.

Step 7
Regional Processor B stores the message temporarily.

Step 8
Regional Processor B assigns a unique ID MON (Message Output Number) to the message and sends it to Slice Processor B.

Step 9
Slice Processor B validates MON.

Step 10
Slice Processor B authorizes Regional Processor B to send the message to Bank B.

Step 11
Regional Processor B sends the message to Bank B.

Step 12
Bank B receives the message and stores it.

Step 13
Bank B sends UAK/UNK to Regional Processor B. UAK (user positive acknowledgment) means Bank B received the message without error; UNK (user negative acknowledgment) means Bank B received checksum failure.

Step 14
Regional Processor B creates a report based on Bank B’s response, and sends it to Slice Processor B.
---
#

# Report Processing Steps

# Report Processing Steps

Step
Action

Step 15
Slice Processor B stores the report.

Step 16 - 17
Slice Processor B sends a copy of the report to Slice Processor A. Slice Processor A stores the report.

Check out our bestselling system design books.

Paperback: Amazon

Digital: ByteByteGo

Page: 79
---
#

# Message Delivery Semantics

# Message Delivery Semantics

In modern architecture, systems are broken up into small and independent building blocks with well-defined interfaces between them. Message queues provide communication and coordination for those building blocks. Today, let’s discuss different delivery semantics: at-most once, at-least once, and exactly once.

# At-most once

As the name suggests, at-most once means a message will be delivered not more than once. Messages may be lost but are not redelivered. This is how at-most once delivery works at the high level.

# Use cases:

- It is suitable for use cases like monitoring metrics, where a small amount of data loss is acceptable.

# At-least once

With this data delivery semantic, it’s acceptable to deliver a message more than once, but no message should be lost.

# Use cases:

- With at-least once, messages won’t be lost but the same message might be delivered multiple times. While not ideal from a user perspective, at-least once delivery semantics are usually good enough for use cases where data duplication is not a big issue or deduplication.
---
#

# Question

# Question:

What is the difference between message queues vs event streaming platforms such as Kafka, Apache Pulsar, etc?
---
#

# Partitioning in Databases

# Partitioning in Databases

# Vertical Partitioning

In vertical partitioning, some columns are moved to new tables. Each table contains the same number of rows but fewer columns.

# Horizontal Partitioning (Sharding)

Horizontal partitioning divides a table into multiple smaller tables. Each table is a separate data store and contains the same number of columns but fewer rows.

# Examples of Horizontal Partitioning:

Database
User ID
Name
Status
Description
Photo

User Table
Bob

User Table
Ted

Horizontal Partition (Hash based)

Database
User ID
Name
Status
Description
Photo

User Table - Shard
Alice

User Table - Shard
Lisa

Horizontal Partition (Range based)

Database
User ID
Name
Status
Description
Photo

User Table - Shard
Bob

User Table - Shard
Alice

Horizontal Partition (Range based)

Database
User ID
Name
Status
Description
Photo

User Table - Shard 2
Ted

User Table - Shard 2
Lisa
---
#

# Data Partitioning

# Data Partitioning

Horizontal partitioning is widely used so let’s take a closer look.

# Routing Algorithm

Routing algorithm decides which partition (shard) stores the data.

# Range-based Sharding

This algorithm uses ordered columns, such as integers, longs, timestamps, to separate the rows. For example, User IDs 1 and 2 are in shard 1, User IDs 3 and 4 are in shard 2.

# Hash-based Sharding

This algorithm applies a hash function to one column or several columns to decide which row goes to which table. For example, User IDs 1 and 3 are in shard 1, User IDs 2 and 4 are in shard 2.

# Benefits

- Facilitate horizontal scaling. Sharding facilitates the possibility of adding more machines to spread out the load.
- Shorten response time. By sharding one table into multiple tables, queries go over fewer rows, and results are returned much more quickly.

# Drawbacks

- The order by operation is more complicated. Usually, we need to fetch data from different shards and sort the data in the application's code.
- Uneven distribution. Some shards may contain more data than others (this is also called the hotspot).

This topic is very big and I’m sure I missed a lot of important details. What else do you think is important for data partitioning?

Reference: 83
---
#

# CDN - Content Delivery Network

# Content Delivery Network (CDN)

A content delivery network (CDN) refers to a geographically distributed network of servers (also called edge servers) which provide fast delivery of static and dynamic content.

Let's take a look at how it works:

# How does CDN work

Suppose Bob who lives in New York wants to visit an eCommerce website that is deployed in London. If the request goes to servers located in London, the response will be quite slow. So we deploy CDN servers close to where Bob lives, and the content will be loaded from the nearby CDN server.

The diagram below illustrates the process:

Step
Description

1
Bob types in www.myshop.com in the browser. The browser looks up the domain name in the local DNS cache.

2
Lookup NNW.myshop.com in DNS Cache and resolve to nearby CDN IP NNW.myshop.cdn.com

3
Resolve Www.myshop.cdn.com to Authoritative Name Server for CDN - Www_myshop.lb.com

4
Return nearby CDN IP from CDN Load Balancer - Www.myshop.lb.com

5
Visit CDN edge node in NY, which is part of the CDN Geo-hierarchy

6
CDN edge node in NY pulls the content from the Web Server (Content Origin) in London
---
#

# DNS Resolution Process

# DNS Resolution Process

Step
Description

2
If the domain name does not exist in the local DNS cache, the browser goes to the DNS resolver to resolve the name. The DNS resolver usually sits in the Internet Service Provider (ISP).

3
The DNS resolver recursively resolves the domain name and then asks the authoritative name server to resolve the domain name.

4
If CDN is not used, the authoritative name server returns the IP address for www.myshop.com. With CDN, the authoritative name server has an alias pointing to www.myshop.cdn.com.

5
The DNS resolver asks the authoritative name server to resolve www.myshop.cdn.com.

6
The authoritative name server returns the domain name for the load balancer of CDN www.myshop.lb.com.

7
The DNS resolver asks the CDN load balancer to resolve www.myshop.lb.com. The load balancer chooses an optimal CDN edge server based on various factors.

8
The CDN load balancer returns the CDN edge server’s IP address for www.myshop.lb.com.

9
The DNS resolver finally returns the IP address to the browser.

10
The browser visits the CDN edge server to load the content, which can be static or dynamic.

11
If the content is not found in the edge CDN server cache, it goes upward to the regional CDN server and then to the central CDN server or even to the origin server.
---
#

# Question

# Question:

How do you prevent videos cached on CDN from being pirated?
---
#

# Erasure Coding

# Erasure Coding

A really cool technique that’s commonly used in object storage such as S3 to improve durability is called Erasure Coding. Let’s take a look at how it works.

# Data Distribution

Split into equal-sized data chunks
Calculate parities
Data loss due to node crash
Data reconstruction

d2
p2
d4
d3

d3
p2
d4
d3

d4

d4

Figure: 3-copy replication - Data is distributed across 3 nodes each with 1GB storage.

Data is distributed across 6 nodes using Erasure Coding (4+2).

Figure 2
---
#

# Erasure Coding and Data Durability

# Erasure Coding and Data Durability

Erasure coding deals with data durability differently from replication. It chunks data into smaller pieces (placed on different servers) and creates parities for redundancy. In the event of failures, we can use chunk data and parities to reconstruct the data.

Question 1: How does erasure coding handle data durability compared to replication?

Answer 1: Erasure coding breaks data into smaller pieces and creates parities for redundancy, allowing for data reconstruction in case of failures.

Question 2: Explain the process of reconstructing lost data in erasure coding.

Answer 2: By using the mathematical formulas and known values of data chunks and parities, lost data can be reconstructed in erasure coding.

Question 3: What is the storage overhead of erasure coding compared to 3-copy replication?

Answer 3: Erasure coding has a storage overhead of 50% (one parity block for every two data chunks), while 3-copy replication has a storage overhead of 200%.

Question 4: Does erasure coding increase data durability?

Answer 4: Yes, erasure coding can achieve higher durability compared to 3-copy replication, as demonstrated by Backblaze's calculation of 11 nines durability for erasure coding and 6 nines durability for 3-copy replication.

Question 5: What other techniques are important for improving the scalability and durability of an object store like S3?

Answer 5: Other important techniques include data partitioning, load balancing, data replication across multiple regions, and efficient error detection and correction mechanisms.
---
#

# Foreign Exchange in Payment

# Foreign Exchange in Payment

Have you wondered what happens under the hood when you pay with USD online and the seller from Europe receives EUR (euro)? This process is called foreign exchange.

JUSD certificate
EUR certificate

deposit
deposit

USD
EUR

USD
EUR

|Funding Pool|
|---|
|USD Account|EUR Account|
|Efi|Sell USD|Buy EUR|

|PayPal|
|---|
|PayPal's USD Account|PayPal's USD Account|PayPal's EUR Account|PayPal's EUR Account|

Suppose Bob (the buyer) needs to pay 100 USD to Alice (the seller), and Alice can only receive EUR. The diagram below illustrates the process.

1. Bob sends 100 USD via a third-party payment provider. In our example, it is Paypal. The money is transferred from Bob’s bank account (Bank B) to Paypal’s account in Bank P1.
2. Paypal needs to convert USD to EUR. It leverages the foreign exchange provider (Bank E). Paypal sends 100 USD to its USD account in Bank E.
---
#

# Foreign Currency Exchange Process

# Foreign Currency Exchange Process

3. 100 USD is sold to Bank E’s funding pool.

4. Bank E’s funding pool provides 88 EUR in exchange for 100 USD. The money is put into Paypal’s EUR account in Bank E.

5. Paypal’s EUR account in Bank P2 receives 88 EUR.

6. 88 EUR is paid to Alice’s EUR account in Bank A.

Now let’s take a close look at the foreign exchange (forex) market. It has 3 layers:

- Retail market. Funding pools are parts of the retail market. To improve efficiency, Paypal usually buys a certain amount of foreign currencies in advance.
- Wholesale market. The wholesale business is composed of investment banks, commercial banks, and foreign exchange providers. It usually handles accumulated orders from the retail market.
- Top-level participants. They are multinational commercial banks that hold a large number of certificates of deposit from different countries. They exchange these certificates for foreign exchange trading.

When Bank E’s funding pool needs more EUR, it goes upward to the wholesale market to sell USD and buy EUR. When the wholesale market accumulates enough orders, it goes upward to top-level participants. Steps 3.1-3.3 and 4.1-4.3 explain how it works.

If you have any questions, please leave a comment.

Question: What foreign currency did you find difficult to exchange? And what company have you used for foreign currency exchange?

Answer: The foreign currency that was difficult to exchange was USD for EUR. The company used for foreign currency exchange was Bank E's funding pool.
---
#

# Interview Question: Design S3

# Interview Question: Design S3

What happens when you upload a file to Amazon S3? Let’s design an S3 like object storage system.

# Upload a File to S3

|Data|Metadata|
|---|---|
|0110101010110|1818010181801|
|Bucket Name|Policy|
|Life Cycle|Metadata|
|Bucket|Object|
|Object Name|Version ID|
|Expiration|Access Control|
|Bucket| |

HTTP PUT:

- Create bucket - HTTP PUT: Ibucket-to-share
- Create object - HTTP PUT: script.txt

Load balancer - Identity validation and authorization

API Service - Identity & Access Management

Storage Node - Primary and Secondary

Service - Upload object, Data

Metadata Service - Create bucket metadata, Create object metadata

Data Store - Metadata DB, Metadata Store

Before we dive into the design, let’s define some terms.
---
#

# S3 Object Storage

# S3 Object Storage

Bucket: A logical container for objects. The bucket name is globally unique. To upload data to S3, we must first create a bucket.

Object: An object is an individual piece of data we store in a bucket. It contains object data (also called payload) and metadata. Object data can be any sequence of bytes we want to store. The metadata is a set of name-value pairs that describe the object.

An S3 object consists of:

- Metadata: It is mutable and contains attributes such as ID, bucket name, object name, etc.
- Object data: It is immutable and contains the actual data.

In S3, an object resides in a bucket. The path looks like this: /bucket-to-share/script.txt. The bucket only has metadata. The object has metadata and the actual data.

The diagram below illustrates how file uploading works:

1. The client sends an HTTP PUT request to create a bucket named "bucket-to-share." The request is forwarded to the API service.
2. The API service calls the Identity and Access Management (IAM) to ensure the user is authorized and has WRITE permission.
3. The API service calls the metadata store to create an entry with the bucket info in the metadata database. Once the entry is created, a success message is returned to the client.
4. After the bucket is created, the client sends an HTTP PUT request to create an object named "script.txt."
5. The API service verifies the user's identity and ensures the user has WRITE permission on the bucket.

Figure 1: Diagram illustrating the file uploading process.
---
#

# API Service Process

# API Service Process

|Step|Description|
|---|---|
|6|Once validation succeeds, the API service sends the object data in the HTTP PUT payload to the data store. The data store persists the payload as an object and returns the UUID of the object.|
|7|The API service calls the metadata store to create a new entry in the metadata database. It contains important metadata such as the object_id (UUID), bucket_id (which bucket the object belongs to), object_name, etc.|
---
#

# Storage Options Comparison

# Storage Options Comparison

Block storage
File storage
Object storage

Mutable Content

N (object versioning is supported, in-place update is not)

Cost
High
Medium to high
Low

Performance
Medium to high, very high
Medium to high
Low to medium

Consistency
Strong consistency
Strong consistency
Strong consistency

Data access
SAS/I iSCSI/FC
Standard file access, CIFS/SMB, and NFS
RESTful API

Scalability
Medium scalability
High scalability
Vast scalability

Good for
Virtual machines (VM); high-performance applications like database
General-purpose file system access
Binary data, unstructured data
---
#

# Storage Systems Overview

# Storage Systems Overview

In this post, let’s review the storage systems in general.

Storage systems fall into three broad categories:

Block storage
File storage
Object storage

Block storage came first, in the 1960s. Common storage devices like hard disk drives (HDD) and solid-state drives (SSD) that are physically attached to servers are all considered as block storage.

Block storage presents the raw blocks to the server as a volume. This is the most flexible and versatile form of storage. The server can format the raw blocks and use them as a file system, or it can hand control of those blocks to an application. Some applications like a database or a virtual machine engine manage these blocks directly in order to squeeze every drop of performance out of them.

Block storage is not limited to physically attached storage. Block storage could be connected to a server over a high-speed network or over industry-standard connectivity protocols like Fibre Channel (FC)
---
#

# Storage Concepts

# Storage Concepts

# Question 1:

What is the main characteristic of block storage?

1. It provides a hierarchical directory structure.
2. It is a shared resource.
3. It presents raw blocks to servers.

Answer: It presents raw blocks to servers.

# Question 2:

Which storage solution is commonly accessed using SMB/CIFS and NFS protocols?

1. Block storage
2. File storage
3. Object storage

Answer: File storage

# Question 3:

What is the main purpose of object storage?

1. High performance
2. Low cost
3. Archival and backup

Answer: Archival and backup
---
#

# DNS Lookup

# Domain Name System (DNS) lookup

DNS acts as an address book. It translates human-readable domain names (google.com) to machine-readable IP addresses (142.251.46.238).

To achieve better scalability, the DNS servers are organized in a hierarchical tree structure.

There are 3 basic levels of DNS servers:

1. Root name server (.): It stores the IP addresses of Top Level Domain (TLD) name servers. There are 13 logical root name servers globally.
2. TLD name server: It stores the IP addresses of authoritative name servers. There are several types of TLD names. For example, generic TLD (.com, .org), country code TLD (.us), test TLD (.test).
3. Authoritative name server: It provides actual answers to the DNS query. You can register authoritative name servers with domain name registrar such as GoDaddy, Namecheap, etc.

The diagram below illustrates how DNS lookup works under the hood:

How does DNS resolve IP

Browser
142.251.46.238

DNS Resolver
Wwwgoogle.com Go to name server for .com

Top Level Domain (TLD) Name Server
WWT.googicom Go to name server com | for google.com

Authoritative Name Server
wwwgoogle com google.com_ ftxus_ 142.251.46.238

1. google.com is typed into the browser, and the browser sends the domain name to the DNS resolver.
---
#

# DNS Resolution Process

# DNS Resolution Process

Step
Description

2
The resolver queries a DNS root name server.

3
The root server responds to the resolver with the address of a TLD DNS server. In this case, it is .com.

4
The resolver then makes a request to the .com TLD.

5
The TLD server responds with the IP address of the domain’s name server, google.com (authoritative name server).

6
The DNS resolver sends a query to the domain’s nameserver.

7
The IP address for google.com is then returned to the resolver from the nameserver.

8
The DNS resolver responds to the web browser with the IP address (142.251.46.238) of the domain requested initially.

DNS lookups on average take between 20-120 milliseconds to complete (according to YSlow).
---
#

# URL Typing Process

# What happens when you type a URL into your browser?

The diagram below illustrates the steps:

URL Components
Explanation

Scheme
http://example.com/product/electric/phone

Domain
example.com

Path
product/electric/phone

Resource
phone

1. Bob enters a URL into the browser and hits Enter. In this example, the URL is composed of 4 parts:
- Scheme - https://. This tells the browser to send a connection to the server using HTTPS.
- Domain - example.com. This is the domain name of the site.
- Path - product/electric/phone. It is the path on the server to the requested resource: phone.
- Resource - phone. It is the name of the resource Bob wants to visit.
2. The browser looks up the IP address for the domain with a domain name system (DNS) lookup. To make the lookup process fast, data is cached at different layers: browser cache, OS cache, local network cache, and ISP cache.
---
#
# Quiz on Web Browsing

# Questions:

|1. What does the browser do if the IP address cannot be found at any of the caches?|Go to DNS servers to do a recursive DNS lookup|
|---|---|
|2. What is the next step after obtaining the IP address of the server?|Establish a TCP connection with the server|
|3. How does the browser send a request to the server?|HTTP request|
|4. What is the status code for a successful response from the server?|200|

# Answers:

1. Go to DNS servers to do a recursive DNS lookup
2. Establish a TCP connection wip pe server
3. HTTP request
4. 200
---
#

# AI Coding Engine

# AI Coding Engine

DeepMind says its new AI coding engine (AlphaCode) is as good as an average programmer.

The AI bot participated in the 10 Codeforces coding competitions and was ranked 54.3%. It means its score exceeded half of the human contestants. If we look at its score for the last 6 months, AlphaCode ranks at 28%.

# How the AI Bot Works

|DATA|SAMPLING|EVALUATION|
|---|---|---|
|GitHub Solutions|CodeContests Problems|Codeforces Problems|
|LEARNING|of potential solutions|Selected candidates|
|Pre-training|Fine-tuning|Large scale sampling|
|1. Pre-train the transformer models on GitHub code.| | |
|2. Fine-tune the models on the relatively small competitive programming dataset.| | |
|3. At evaluation time, create a massive amount of solutions for each problem.| | |
|4. Filter, cluster and rerank the solutions to a small set of candidate programs (at most 10), and then submit for further assessments.| | |
|5. Run the candidate programs against the test cases, evaluate the performance, and choose the best one.| | |
---
#

# AI Bot vs Software Engineers

# Question:

Do you think AI bot will be better at Leetcode or competitive programming than software engineers five years from now?

# Options:

|1.|Yes|
|---|---|
|2.|No|
---
#

# Read Replica Pattern

# Read Replica Pattern

There are two common ways to implement the read replica pattern:

1. Embed the routing logic in the application code (explained in the last post).
2. Use database middleware.

We will focus on option 2 here. The middleware provides transparent routing between the application and database servers. Customization of the routing logic can be based on various rules such as user, schema, statement, etc.

The diagram below illustrates the setup:

|Database Middleware|blog bytebytego.com|
|---|---|
|Alice|Place an order|
|Order Service|Database operations|
|MySQL Network Protocol|Database Middleware|
|Read View|Write View|
|Order history|Create an order|
|Replication|Replication|
|Secondary DB 2|Primary DB|Secondary DB 1|
|MySQL Database Cluster| |

Diagram Key:

- Read: View order history
- Write: Create an order
- Read: View order details
---
#

# Database Middleware Information

# Database Middleware Information

Question
Answer

1. What happens when Alice places an order on Amazon?
The request is sent to Order Service.

2. How does Order Service interact with the database?
It sends database queries to the database middleware.

3. What role does the database middleware play in the system?
It routes writes to the primary database and replicates data to two replicas.

4. How does Alice view the order details?
The request is sent through the middleware.

5. How does Alice view the recent order history?
The request is sent through the middleware.

6. What communication protocol does the database middleware use?
It uses the standard MySQL network protocol for communication.

Pros of using a database middleware:
- Simplified application code.
- Better compatibility with MySQL network protocol.

Cons of using a database middleware:
- Increased system complexity.
- Additional network latency.

Note: The database middleware acts as a proxy between the application and databases.
---
#

# Read Replica Pattern

# Read Replica Pattern

In this post, we talk about a simple yet commonly used database design pattern (setup): Read replica pattern.

In this setup, all data-modifying commands like insert, delete, or update are sent to the primary DB, and reads are sent to read replicas.

The diagram below illustrates the setup:

Step
Description

1
When Alice places an order on amazon.com, the request is sent to Order Service.

2
Order Service creates a record about the order in the primary DB (write). Data is replicated to two replicas.

3
Alice views the order details. Data is served from a replica (read).

4
Alice views the recent order history. Data is served from a replica (read).

There is one major problem in this setup: replication lag.

Diagram:
---
#

# Read-After-Write Consistency

# Read-After-Write Consistency

Under certain circumstances (network delay, server overload, etc.), data in replicas might be seconds or even minutes behind. In this case, if Alice immediately checks the order status (query is served by the replica) after the order is placed, she might not see the order at all. This leaves Alice confused. In this case, we need “read-after-write” consistency.

# Possible solutions to mitigate this problem:

|Option|Description|
|---|---|
|1|Latency sensitive reads are sent to the primary database.|
|2|Reads that immediately follow writes are routed to the primary database.|
|3|A relational DB generally provides a way to check if a replica is caught up with the primary. If data is up to date, query the replica. Otherwise, fail the read request or read from the primary.|
---
#

# Email Receiving Flow

# Email Receiving Flow

The following diagram demonstrates the email receiving flow:

|Step|Description|
|---|---|
|1|Incoming emails arrive at the SMTP load balancer.|
|2|The load balancer distributes traffic among SMTP servers. Email acceptance policy can be configured and applied at the SMTP-connection level. Invalid emails are bounced to avoid unnecessary email processing.|
|3|If the attachment of an email is too large to put into the queue, it is stored in the attachment store (S3).|
|4|Emails are put in the incoming email queue. The queue decouples mail processing workers from SMTP servers for independent scaling and serves as a buffer in case of email volume surges.|
|5|Mail processing workers handle tasks like filtering out spam mails and stopping viruses. This assumes the email passed validation.|
|6|The email is stored in the mail storage, cache, and object data store.|
---
#

# Email Communication Process

# Email Communication Process

|Question|Answer|
|---|---|
|What happens if the receiver is currently online?|The email is pushed to real-time servers.|
|What are real-time servers?|WebSocket servers that allow clients to receive new emails in real-time.|
|What happens to emails for offline users?|Emails are stored in the storage layer.|
|How does the webmail client connect to web servers for offline users?|It connects via RESTful API when the user comes back online.|
|How do web servers deliver new emails to the client for offline users?|They pull new emails from the storage layer and return them to the client.|
---
#

# Email Sending Flow

# Email Sending Flow

|Step|Description|
|---|---|
|1|A user writes an email on webmail and presses the “send” button. The request is sent to the load balancer.|
|2|The load balancer makes sure it doesn’t exceed the rate limit and routes traffic to web servers.|
|3|Web servers are responsible for: - Basic email validation. Each incoming email is checked against pre-defined rules such as email size limit.
- Checking if the domain of the recipient’s email address is the same as the sender. If it is the same, email data is inserted to storage, cache, and object store directly. The recipient can fetch the email directly via the RESTful API. There is no need to go to step 4.
|
|4|Message queues.|
---
#

# Email Processing Workflow

# Email Processing Workflow

|Step|Description|
|---|---|
|4.a|If basic email validation succeeds, the email data is passed to the outgoing queue.|
|4.b|If basic email validation fails, the email is put in the error queue.|
|5|SMTP outgoing workers pull events from the outgoing queue and make sure emails are spam and virus free.|
|6|The outgoing email is stored in the “Sent Folder” of the storage layer.|
|7|SMTP outgoing workers send the email to the recipient mail server.|

Each message in the outgoing queue contains all the metadata required to create an email. A distributed message queue is a critical component that allows asynchronous mail processing. By decoupling SMTP outgoing workers from the web servers, we can scale SMTP outgoing workers independently.

We monitor the size of the outgoing queue very closely. If there are many emails stuck in the queue, we need to analyze the cause of the issue. Here are some possibilities:

- The recipient’s mail server is unavailable. In this case, we need to retry sending the email at a later time. Exponential backoff might be a good retry strategy.
- Not enough consumers to send emails. In this case, we may need more consumers to reduce the processing time.

Note: The total number of steps in the email processing workflow is 7.
---
#

# Interview Question: Design Gmail

# Interview Question: Design Gmail

One picture is worth more than a thousand words. In this post, we will take a look at what happens when Alice sends an email to Bob.

|User Alice|User Bob|
|---|---|
|alice@outlook.com|bob@gmail.com|
|Outlook client|Gmail client|

1. Alice logs in to her Outlook client, composes an email, and presses “send”. The email is sent to the Outlook mail server. The communication protocol between the Outlook client and mail server is SMTP.

2. Outlook mail server queries the DNS (not shown in the diagram) to find the address of the recipient’s SMTP server. In this case, it is Gmail’s SMTP server. Next, it transfers the email to the Gmail mail server. The communication protocol between the mail servers is SMTP.

3. The Gmail server stores the email and makes it available to Bob, the recipient.
---
#

# Email Fetching Process

# Email Fetching Process

|Step|Description|
|---|---|
|1|Gmail client fetches new emails|
|2|IMAP/POP server is accessed|
|3|Bob logs in to Gmail|

This process is a simplified design. Each component can be explained in more depth in the future.

Hope this sparks your interest and curiosity :)

Reference: 112
---
#

# Map Rendering and Road Segments

# Map Rendering

Let's explore the concept of Map Rendering in this post.

# Pre-Computed Tiles

One foundational concept in map rendering is tiling. The world is divided into smaller tiles at different zoom levels. Google Maps, for example, uses 21 zoom levels.

|Zoom Level|Number of Tiles|Tile Size|
|---|---|---|
|0|1|256 x 256 pixels|
|1|4|512 x 512 pixels|
|2|16|1024 x 1024 pixels|

This tiling approach allows for rendering maps at different granularities based on the client's zoom level, optimizing bandwidth usage.

# Road Segments

In addition to map tiles, defining road segments is crucial for navigation algorithms.

We divide roads into small blocks called road segments, which contain multiple roads, junctions, and metadata.

These road segments are grouped into super segments for better coverage and transformed into a graph data structure for navigation algorithms.

In the graph, nodes represent road segments, and two nodes are connected if the corresponding road segments are reachable.
---
#

# Text Recognition

# Text Recognition

How can we approach finding a path between two locations using neighbors?

What algorithms can be leveraged for solving the shortest-path problem?

Fill in the blank: Finding a path between two locations becomes a __________-path problem.

What are two algorithms that can be used to solve the shortest-path problem?

Answer: Dijkstra or A* algorithms.
---
#

# Interview Question: Design Google Maps

# Interview Question: Design Google Maps

Google started project Google Maps in 2005. As of March 2021, Google Maps had one billion daily active users, 99% coverage of the world in 200 countries.

Although Google Maps is a very complex system, we can break it down into 3 high-level components. In this post, let’s take a look at how to design a simplified Google Maps.

|Component|Description|
|---|---|
|Mobile User|Interacts with the Google Maps application on their mobile devices.|
|Load Balancer|Manages the distribution of incoming traffic across multiple servers to ensure efficient use of resources.|
|CDN|Content Delivery Network helps in delivering content, including static map images, to users efficiently.|
|Navigation Service|Provides directions and routes to users based on their input.|
|Location Service|Helps in determining the current location of the user and providing relevant information.|
|Geocoding DB|Database that translates addresses into geographic coordinates.|
|Road Segment DB|Stores information about road segments, traffic conditions, etc.|
|User Location DB|Keeps track of user locations and preferences for personalized services.|
|Static Map Images (Object Storage)|Stores static map images that are served to users.|

Designing Google Maps involves integrating these components effectively to provide a seamless mapping experience to users.
---
#

# Location Service

# Location Service

The location service is responsible for recording a user’s location update. The Google Map clients send location updates every few seconds. The user location data is used in many cases:

- Detect new and recently closed roads
- Improve the accuracy of the map over time
- Used as an input for live traffic data

# Map Rendering

The world’s map is projected into a huge 2D map image. It is broken down into small image blocks called “tiles” (see below). The tiles are static. They don’t change very often. An efficient way to serve static tile files is with a CDN backed by cloud storage like S3. The users can load the necessary tiles to compose a map from nearby CDN.

What if a user is zooming and panning the map viewpoint on the client to explore their surroundings?

An efficient way is to pre-calculate the map blocks with different zoom levels and load the images when needed.

# Navigation Service

This component is responsible for finding a reasonably fast route from point A to point B. It calls two services to help with the path calculation:

1. Geocoding Service: resolve the given address to a latitude/longitude pair
2. Route Planner Service: this service does three things in sequence:
1. Calculate the top-K shortest paths between A and B
2. Calculate the estimation of time for each path based on current traffic and historical data
3. Rank the paths by time predictions and user filtering. For example, the user doesn’t want to avoid tolls.
---
#

# Pull vs Push Models

# Pull vs Push Models

There are two ways metrics data can be collected, pull or push. It is a routine debate as to which one is better and there is no clear answer. In this post, we will take a look at the pull model.

Metrics Source
Service Discovery

Web Servers
Kubernetes Zookeeper

DB Clusters
Pull metrics Metrics Collector

Queue Clusters
Pull metrics

Cache Clusters
Pull metrics

Figure 1: Region - US-west

Service Discovery

Kubernetes Zookeeper

Discover Targets
Metrics Collector

Figure 2: Region - US-south, US-east, Type - MySQL, Host - 10.10.11.1

Web Servers
HTTP Requests

Metrics Endpoint

Figure 3
---
#

# Data Collection with Pull Model over HTTP

# Data Collection with Pull Model over HTTP

Figure 1 shows data collection with a pull model over HTTP. We have dedicated metric collectors which pull metrics values from the running applications periodically.

In this approach, the metrics collector needs to know the complete list of service endpoints to pull data from. One naive approach is to use a file to hold DNS/IP information for every service endpoint on the "metric collector" servers. While the idea is simple, this approach is hard to maintain in a large-scale environment where servers are added or removed frequently, and we want to ensure that metric collectors don't miss out on collecting metrics from any new servers.

The good news is that we have a reliable, scalable, and maintainable solution available through Service Discovery, provided by Kubernetes, Zookeeper, etc., wherein services register their availability and the metrics collector can be notified by the Service Discovery component whenever the list of service endpoints changes. Service discovery contains configuration rules about when and where to collect metrics as shown in Figure 2.

Figure 3 explains the pull model in detail.

# Key Points:

1. The metrics collector fetches configuration metadata of service endpoints from Service Discovery. Metadata include pulling interval, IP addresses, timeout and retries parameters, etc.
2. The metrics collector pulls metrics data via a pre-defined HTTP endpoint (for example, /metrics). To expose the endpoint, a client library usually needs to be added to the service. In Figure 3, the service is Web Servers.
3. Optionally, the metrics collector registers a change event notification with Service Discovery to receive an update whenever the service endpoints change. Alternatively, the metrics collector can poll for endpoint changes periodically.

For more details and visual representation, please refer to the original document.

Reference: Page 118
---
#

# Money Movement

# Money Movement

One picture is worth more than a thousand words. This is what happens when you buy a product using Paypal/bank card under the hood.

To understand this, we need to digest two concepts: clearing & settlement. Clearing is a process that calculates who should pay whom with how much money; while settlement is a process where real money moves between reserves in the settlement bank.

| |Clearing|Settlement|Info|
|---|---|---|---|
| |Transactions|Clearing Institution|Clearing Institution|
| |Bob's Account|Transfer Request| |
|Amazon's Account| |Transfer Request| |
|Claire's Account| |Transfer Request| |

FME

IBLLD

Reserve

Reserve

Reserve

Clearing_settlement info

Clearing_settlement into

2.3 Transactions

Transfer Request

Buy a book

Send the money

Pay-in flow

Pay-out flow
---
#

# SDI Book Purchase Process

# SDI Book Purchase Process

# Pay-in flow (Bob pays Amazon money):

Step
Description

1.1
Bob buys a book on Amazon using Paypal.

1.2
Amazon issues a money transfer request to Paypal.

1.3
Paypal transfers money from Bob's debit card to Amazon's bank account in Bank A.

1.4
Transaction statements are sent to the clearing institution, which reduces the transactions to be settled.

1.5 & 1.6
The clearing institution sends clearing and settlement information to the settlement bank for actual money movement between reserve accounts.

# Pay-out flow (Amazon pays the money to the seller - Claire):

Step
Description

2.1
Amazon informs the seller (Claire) about the upcoming payment.

2.2
Amazon requests a money transfer from Bank A to the seller's bank (Bank C).

2.3
Transaction statements are sent to the clearing institution by both Bank A and Bank C.

2.4 & 2.5
The clearing institution sends clearing and settlement information to transfer money from Bank A's reserve to Bank C's reserve.

Layers involved:

- Transaction layer: where online purchases occur
- Payment and clearing layer: where payment instructions and transaction netting occur
- Settlement layer: where actual money movement happens
---
#

# Information Flow and Fund Flow

# Information Flow and Fund Flow

The first two layers are called information flow, and the settlement layer is called fund flow.

You can see the information flow and fund flow are separated. In the info flow, the money seems to be deducted from one bank account and added to another bank account, but the actual money movement happens in the settlement bank at the end of the day.

Because of the asynchronous nature of the info flow and the fund flow, reconciliation is very important for data consistency in the systems along with the flow.

It makes things even more interesting when Bob wants to buy a book in the Indian market, where Bob pays USD but the seller can only receive INR.
---
#

# Reconciliation Problems in Payment Processing

# Reconciliation Problems in Payment Processing

My previous post about painful payment reconciliation problems sparked lots of interesting discussions. One of the readers shared more problems we may face when working with intermediary payment processors in the trenches and a potential solution:

# 1. Foreign Currency Problem:

When you operate a store globally, you will come across this problem quite frequently. If the transaction happens in a currency different from the standard currency of the payment processor, it creates an additional layer of complexity. There needs to be a reliable way to reconcile currency exchange transactions.

# 2. Multiple Events Triggered by Payment Providers:

Payment providers act as intermediaries, triggering multiple events for a company. For example, a purchase via Paypal can involve the initial transaction, followed by the transfer of funds to a bank account. Reconciling these transactions, especially when different currencies are involved, can be challenging.

# 3. Platform-Specific Buyer Side Issues:

Some problems arise on the buyer side that are platform-specific. For instance, shadow transactions from Paypal can lead to partial payments for subsequent transactions if the initial transaction is not completed or is canceled. This can result in discrepancies in the amount withdrawn from the bank account.

# In practice, this usually looks something like this:

1. Your shop assigns an order number to the purchase
---
#
# Payment Process Overview

# Payment Process Overview

Step 2
The order number is carried over to the payment provider

Step 3
The payment provider creates another internal ID, which is carried over across transactions within the system

Step 4
The payment ID is used when you get the payout on your bank account (or the payment provider bundles individual payments, which can be reconciled within the payment provider system)

Step 5
Ideally, your payment provider and your shop have an integration/API with the tool you use to (hopefully automatically) create invoices. This usually carries over the order id from the shop (closing the loop) and sometimes even the payment id to match it with the invoice id, which you then can use to reconcile it with your accounts receivable/payable.

Credit: A knowledgeable reader who prefers to stay private. Thank you!

Reference Number: 123
---
#

# Database Selection for Metrics Collection Service

# How to Choose the Right Database for Metrics Collecting Service?

When selecting a database for metrics collection service, it is important to consider the specific requirements of your system. Here are some factors to keep in mind:

|Metrics Source|Metrics Collector|Time Series DB|
|---|---|---|
|Email|Kafka|OpenTSDB|
|Text Message|Consumers|InfluxDB|
|Alert System|Query Service|Prometheus|
|PageDuty|Send Queries| |
| |HTTPS Endpoints| |
| |Visualization System| |

There are various time-series databases optimized for handling large volumes of data efficiently. Some popular options include:

- OpenTSDB: A distributed time-series database based on Hadoop and HBase, suitable for handling complex data.
- InfluxDB: Known for its ability to store large volumes of time-series data and perform real-time analysis effectively.
- Prometheus: Another popular choice for real-time analysis and efficient data storage.

It is essential to evaluate the specific needs of your metrics collection service and choose a database that aligns with those requirements.
---
#

# Time-Series Databases Interview Concepts

# Time-Series Databases Interview Concepts

1. What is the importance of understanding that metrics data are time-series in nature for an interview?

Answer: It is important to understand that metrics data are time-series in nature for an interview to select appropriate time-series databases for storage, such as InfluxDB.

2. How does InfluxDB facilitate efficient aggregation and analysis of time-series data?

Answer: InfluxDB builds indexes on labels to enable fast lookup of time-series by labels, ensuring efficient aggregation and analysis of a large amount of time-series data.

3. Why is it crucial for each label in a time-series database to have low cardinality?

Answer: Each label in a time-series database should have low cardinality to ensure a small set of possible values, which is critical for visualization and prevents overloading the database.
---
#

# Metrics Collecting System Database Selection

# Metrics Collecting System Database Selection

# Question:

Which database shall I use for the metrics collecting system?

# Answer:

It is recommended not to build your own storage system or use a general-purpose storage system like MySQL for this job. A general-purpose database, although theoretically capable of supporting time-series data, would require expert-level tuning to handle the scale of data being written and read in this system. Specifically, a relational database is not optimized for operations commonly performed on time-series data, such as computing moving averages in rolling time windows and supporting tagging/labeling data efficiently. Additionally, general-purpose relational databases do not perform well under constant heavy write loads, requiring significant tuning efforts that may still not yield satisfactory performance at the required scale.

# Data Access Pattern:

Each label on the y-axis represents a time series uniquely identified by names and labels, while the x-axis represents time. The write load is heavy with millions of operational metrics written per day, and many metrics collected at high frequency, making the system write-heavy. The read load is spiky, influenced by visualization and alert services querying the database, resulting in bursty read volumes.
---
#

# Time-Series Databases

# Time-Series Databases

1. What are some NoSQL databases that can handle time-series data effectively?

Answer: Cassandra and Bigtable

2. Why is using a general purpose NoSQL database not appealing for time-series data?

Answer: Industrial-scale time-series databases are readily available and optimized for time-series data storage and querying.

3. Name two popular time-series databases according to DB-engines.

Answer: InfluxDB and Prometheus

4. What is a key feature of time-series databases for efficient data analysis?

Answer: Efficient aggregation and analysis of a large amount of time-series data by labels or tags.

5. How does InfluxDB facilitate fast lookup of time-series data?

Answer: InfluxDB builds indexes on labels to facilitate fast lookup of time-series data.
---
#

# Labels Best Practice Guidelines

# Labels Best Practice Guidelines

It provides clear best-practice guidelines on how to use labels, without overloading the database. The key is to make sure each label is of low cardinality (having a small set of possible values). This feature is critical for visualization, and it would take a lot of effort to build this with a general-purpose database.

|Question|Answer|
|---|---|
|What is the key to using labels effectively?|The key is to make sure each label is of low cardinality, meaning it has a small set of possible values.|
|Why is having low cardinality labels important?|Low cardinality labels are critical for visualization and prevent overloading the database.|
|Why would it take a lot of effort to build this feature with a general-purpose database?|Building low cardinality labels for visualization would require significant effort with a general-purpose database.|
---
#

# Metrics Monitoring and Alerting System

# Metrics Monitoring and Alerting System

A well-designed metrics monitoring and alerting system plays a key role in providing clear visibility into the health of the infrastructure to ensure high availability and reliability. The diagram below explains how it works at a high level.

Metrics Source
Alert System

Metrics Collector
Send Queries

Kafka
Consumers

Time series DB
Cache

Metrics source: This can be application servers, SQL databases, message queues, etc.

Metrics collector: It gathers metrics data and writes data into the time-series database.

Time-series database: This stores metrics data as time series. It usually provides a custom query interface for analyzing and summarizing a large amount of time-series data. It maintains indexes on labels to facilitate the fast lookup of time-series data by labels.

Kafka: Kafka is used as a highly reliable and scalable distributed messaging platform. It decouples the data collection and data processing services from each other.

Alerting methods include Email, Text Message, PageDuty, HTTPS Endpoints, and Visualization System.

129
---
#
# Time-Series Database Components

# Time-Series Database Components

Component
Description

Consumers
Consumers or streaming processing services such as Apache Storm, Flink and Spark, process and push data to the time-series database.

Query service
The query service makes it easy to query and retrieve data from the time-series database. This should be a very thin wrapper if we choose a good time-series database. It could also be entirely replaced by the time-series database’s own query interface.

Alerting system
This sends alert notifications to various alerting destinations.

Visualization system
This shows metrics in the form of various graphs/charts.
---
#

# Reconciliation Process in Payment Systems

# Reconciliation Process in Payment Systems

Reconciliation might be the most painful process in a payment system. It is the process of comparing records in different systems to make sure the amounts match each other.

|Inside|Outside|
|---|---|
|Payment Service Providers (PSPI)|Card Schemes|
|Payment event|PayPal|
|Payment Service Executor|VISA|
|Ledger|Wallet|
|Settlement file|Reconciliation|
|Account|Debit|
|buyer|$200|
|seller|$200|

For example, if you pay $200 to buy a watch with Paypal:

- The eCommerce website should have a record about the purchase order of $200.
- There should be a transaction record of $200 in Paypal.
- The Ledger should record a debit of $200 dollars for the buyer, and a credit of $200 for the seller. This is called double-entry bookkeeping.

# Pain Points and Solutions

Let’s take a look at some pain points and how we can address them:

1. Pain Point 1
2. Solution 1

Pain Point 2
---
#

# Data Reconciliation Techniques

# Data Reconciliation Techniques

Problem
Possible Solution

Problem 1: Data normalization
When comparing records in different systems with different formats, add a layer to transform them into the same format.

Problem 2: Massive data volume
Use big data processing techniques to speed up data comparisons. For near real-time reconciliation, use a streaming platform like Flink; for end-of-day batch processing, use Hadoop.

Problem 3: Cut-off time issue
Categorize the break as a "temporary break" if there is a discrepancy in cut-off times. Run it later against the next day's records. If a match is found, clear the break.

It is essential to have a reconciliation system in place despite having exactly-once semantics to address discrepancies that may arise in various scenarios.

Having a reconciliation system acts as a safety net, ensuring peace of mind and better sleep at night.

Note: The content above highlights key problems in data reconciliation and their possible solutions.
---
#

# Database Options in Google Cloud

# Database Options in Google Cloud

Choosing the right database is crucial. Google Cloud provides various database options to cater to different use cases. Below is a summary of the available options:

Relational
Non-Relational (NoSQL)
In-Memory

Cloud SQL - Managed MySQL, PostgreSQL, SQL Server
Firestore - Cloud Native, serverless; Cloud Bigtable - Cloud-native NoSQL; Memory Store - Fully managed Redis and Memcached for sub-millisecond latency

Cloud Spanner - Cloud-native with large scale, consistency, global strong consistency, SLA

Bare Metal - Lift and shift Oracle Workloads

General purpose RDBMS + scale, HA, HTAP
RDBMS + scale; HA, HTAP
In-memory and Key-value store

SOLDB - Large scale complex transactional data

Use Cases: OLTP, OLAP, HTAP
Use Cases: Mobile apps, Personalization, Caching, Session store
Use Cases: Gaming, Personalization

ERP, CRM, E-commerce
Global financial ledger, Data center applications
Recommendation, Fraud detection, Social network

Offline sync, Personalized ads, Fraud detection
---
#

# Big Data Papers Timeline

# Big Data Papers Timeline

Big Data Papers
Year

BigTable
2006

Megastore
2011

Spanner
2012

GFS
2003

MapReduce
2004

Hive
2009

Dremel
2010

Storm
2011

Kafka
2011

Kappa
2014

Dataflow Model
2015

Spark
2010

Flink
2015

Chubby
2006

Thrift
2007

Raft
2014

Borg
2015

Kubernetes
2016

The green highlighted boxes are the famous 3 Google papers, which established the foundation of the big data framework. At the high-level:

Big Data Techniques = Massive data + Massive calculation

Let’s look at the OLTP evolution. BigTable provided a distributed storage system for structured data but dropped some characteristics of relational DB. Then Megastore brought back schema and simple transactions; Spanner brought back data consistency.

Now let’s look at the OLAP evolution. MapReduce was not easy to program, so Hive solved this by introducing a SQL-like query.
---
#
# Text Processing Technologies

# Questions:

1. What technology provided an interactive query engine in 2010?
2. Which architecture was based on Storm and MapReduce for solving latency issues in OLAP?
3. When was the Dataflow Model published by Google?
4. What technology is needed to manage a big crowd of commodity server resources?

# Answers:

1. Dremel
2. 𝒍𝒂𝒎𝒃𝒅𝒂 architecture
3. 2015
4. Kubernetes
---
#

# Double Charge Prevention

# Avoid Double Charge

One of the most serious problems a payment system can have is to double charge a customer. When designing the payment system, it is important to guarantee that the payment system executes a payment order exactly-once.

# How to Avoid Double Payment

Client
Payment System
Retry

Pay $10
Payment failed
Retry

Retry
Pay $10
Payment failed

Retry
Pay $10
Payment failed

Retry
Pay $10
Payment succeeded

Idempotency: POST {idempotency-key: UUID}

Client
Payment System

First request
Charge succeeded

Retry
POST {idempotency-key: UUID}

Retry
Return previous message: Server has already seen the idempotency key. Do not process the request again.

By implementing idempotency keys, the payment system can prevent double charges by ensuring that duplicate requests are not processed multiple times.
---
#

# Exactly-Once Delivery

# Exactly-Once Delivery

At the first glance, exactly-once delivery seems very hard to tackle, but if we divide the problem into two parts, it is much easier to solve. Mathematically, an operation is executed exactly-once if:

1. It is executed at least once.
2. At the same time, it is executed at most once.

We now explain how to implement at least once using retry and at most once using idempotency check.

# Retry

Occasionally, we need to retry a payment transaction due to network errors or timeout. Retry provides the at-least-once guarantee. For example, as shown in Figure 10, the client tries to make a $10 payment, but the payment keeps failing due to a poor network connection. Considering the network condition might get better, the client retries the request and this payment finally succeeds at the fourth attempt.

# Idempotency

From an API standpoint, idempotency means clients can make the same call repeatedly and produce the same result.

For communication between clients (web and mobile applications) and servers, an idempotency key is usually a unique value that is generated by clients and expires after a certain period of time. A UUID is commonly used as an idempotency key and it is recommended by many tech companies such as Stripe and PayPal. To perform an idempotent payment request, an idempotency key is added to the HTTP header: &lt;idempotency-key: key_value&gt;.

Reference: Page 137
---
#

# Payment Security Techniques

# Payment Security Techniques

Problem
Solution

Request/response eavesdropping
Use HTTPS

Data tampering
Enforce encryption and integrity monitoring

Man-in-the-middle attack
Use SSL and authentication certificates

Data loss
Database replication across multiple regions and take snapshot of data

Distributed denial-of-service attack (DDoS)
Rate limiting and firewall

Card theft
Tokenization. Instead of using real card numbers, tokens are stored and used for payment

PCI compliance
PCI DSS is an information security standard for organizations that handle branded credit cards

Fraud
Address verification, card verification value (CVV), user behavior analysis, etc.

If you have any questions or if anything was missed, please leave a comment.
---
#
# System Design Interview Tip

# System Design Interview Tip

One pro tip for acing a system design interview is to read the engineering blog of the company you are interviewing with. You can get a good sense of what technology they use, why the technology was chosen over others, and learn what issues are important to engineers.

# Twitter Engineering

@TwitterEng

Interview pro-tip: To those interviewing for our engineering roles, checkout some of these key posts that can help you understand our architecture and prepare for the System Design rounds:

- The Infrastructure Behind Twitter: Scale
- Discovery and Consumption of Analytics Data at Twitter
- The what and why of product experimentation at Twitter
- Twitter experimentation: technical overview

For more information, visit Twitter Engineering
---
#

# Big Data Evolvement

# Big Data Evolvement

I hope everyone has a great time with friends and family during the holidays. If you are looking for some readings, classic engineering papers are a good start.

A lot of times when we are busy with work, we only focus on scattered information, telling us “how” and “what” to get our immediate needs to get things done.

However, reading the classics helps us know “why” behind the scenes, and teaches us how to solve problems, make better decisions, or even contribute to open source projects.

Let’s take big data as an example.

Big data area has progressed a lot over the past 20 years. It started from 3 Google papers (see the links in the comment), which tackled real engineering challenges at Google scale:

- GFS (2003) - big data storage
- MapReduce (2004) - calculation model
- BigTable (2006) - online services

The diagram below shows the functionalities and limitations of the 3 techniques, and how they evolve over time into two streams: OLTP and OLAP. Each evolved product was trying to solve the limitations of the.

140
---
#

# Recommendation for Classic Papers

# Recommendation for Classic Papers

In the last generation, Hive attempted to address the absence of SQL in MapReduce by introducing "Hive - support SQL".

If you are interested in delving deeper into this topic, you can explore the related papers for more detailed information.

Which other classic papers would you suggest for further reading?
---
#

# Quadtree Data Structure

# Quadtree Data Structure

In this post, let’s explore another data structure to find nearby restaurants on Yelp or Google Maps.

A quadtree is a data structure that is commonly used to partition a two-dimensional space by recursively subdividing it into four quadrants (grids) until the contents of the grids meet certain criteria.

Below is a diagram illustrating the process of dividing an area into a quadtree:

|NE (60-)|NW (140)|
|---|---|
|SE (200m)|SW (30m)|
|Represent many layers|Represent many layers|
|Internal node|Leaf node|
---
#

# Quadtree Data Structure

# Quadtree Data Structure

Quadtree is an in-memory data structure and not a database solution. It runs on each LBS (Location-Based Service, see last week’s post) server, and the data structure is built at server start-up time.

The second diagram explains the quadtree building process in more detail. The root node represents the whole world map. The root node is recursively broken down into 4 quadrants until no nodes are left with more than 100 businesses.

# How to get nearby businesses with quadtree?

1. Build the quadtree in memory.
2. After the quadtree is built, start searching from the root and traverse the tree, until we find the leaf node where the search origin is.
3. If that leaf node has 100 businesses, return the node. Otherwise, add businesses from its neighbors until enough businesses are returned.

# Update LBS server and rebuild quadtree

- It may take a few minutes to build a quadtree in memory with 200 million businesses at the server start-up time.
- While the quadtree is being built, the server cannot serve traffic.
- Therefore, we should roll out a new release of the server incrementally to a small subset of servers at a time. This avoids taking a large swathe of the server cluster offline and causes service brownout.
---
#

# Yelp Nearby Restaurants

# How do we find nearby restaurants on Yelp?

Here are some design details behind the scenes:

Key Services
Description

Load Balancer
Responsible for distributing incoming search requests to the appropriate services.

Local Based Service
Provides read and write operations for retrieving and updating restaurant information.

Business Service
Handles specific business-related operations such as retrieving details for a particular restaurant.

Database Cluster
Consists of replicas and a primary database for data storage and retrieval.

Business Service: This service is responsible for handling business-specific operations.

Load Balancer: Distributes incoming search requests to the appropriate services.

Database Cluster: Consists of replicas and a primary database for data storage and retrieval.

Local Based Service: Provides read and write operations for restaurant information.
---
#

# Restaurant Location Storage for LBS

# Restaurant Location Storage for Location-Based Service (LBS)

How are the restaurant locations stored in the database so that LBS can return nearby restaurants efficiently?

Store the latitude and longitude of restaurants in the database? The query will be very inefficient when you need to calculate the distance between you and every restaurant.

One way to speed up the search is using the geohash algorithm.

1. First, divide the planet into four quadrants along with the prime meridian and equator:
- Latitude range [-90, 0] is represented by 0
- Latitude range [0, 90] is represented by 1
- Longitude range [-180, 0] is represented by 0
- Longitude range [0, 180] is represented by 1
2. Second, divide each grid into four smaller grids. Each grid can be represented by alternating between longitude bit and latitude bit.

So when you want to search for the nearby restaurants in a specific block, you can write SQL like:

SELECT * FROM geohash_index WHERE geohash LIKE '01%'
Geohash has some limitations. There can be a lot of restaurants in one block (e.g., downtown New York), but none in another block (e.g., ocean). So there are other more complicated algorithms to optimize the process. Let me know if you are interested in the details.
---
#
# Log4j JNDI Attack and Prevention

# Log4j JNDI Attack and Prevention

One picture is worth more than a thousand words. Log4j from attack to prevention in one illustration.

# The Log4j JNDI Attack and How to Prevent It

Attacker
Vulnerable Server
Vulnerable Log4j Implementation
Malicious LDAP Server

Inserts the JNDI lookup in the header field likely to be logged
http://victimxa
Log4j interpolates the string and queries the malicious LDAP server
ldap://evilxa

BLOCK WITH WAF

PATCH LOG4J

DISABLE JNDI LOOKUPS

DISABLE LOG4J

DISABLE REMOTE CODEBASES

Credit: GovCERT

For more information, visit GovCERT
---
#

# Stock Exchange Microsecond Latency

# How does a modern stock exchange achieve microsecond latency?

The principal is to focus on the critical path:

- Fewer tasks on the critical path
- Less time on each task
- Fewer network hops
- Less disk usage

# Order Manager - Matching Engine - Market Data Publisher

|Order Manager|Matching Engine|Market Data Publisher|
|---|---|---|
|Application Loop|Application Loop|Application Loop|
|Reporter|Logging|Aggregated Risk Check|
| | |Position Keeper|

For the stock exchange, the critical path includes:

1. Start: an order comes into the order manager
2. Mandatory risk checks
3. The order gets matched and the execution is sent back
4. End: the execution comes out of the order manager

Other non-critical tasks should be removed from the critical path.

We put together a design as shown in the diagram:
---
#

# System Architecture Specifications

# System Architecture Specifications

|Specification|Description|
|---|---|
|Server Configuration|Deploy all components in a single giant server without using containers.|
|Communication|Use shared memory as an event bus for communication among components, avoiding the use of hard disk.|
|Key Components|Order Manager and Matching Engine are single-threaded on the critical path, each pinned to a CPU to ensure no context switches and locks.|
|Application Execution|The single-threaded application loop executes tasks sequentially, one by one.|
|Component Interaction|Other components listen on the event bus and react to events accordingly.|

Reference: 148
---
#

# Stock Orders Matching

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Stock Orders Matching

Stock exchanges use the data structure called order books. An order book is an electronic list of buy and sell orders, organized by price levels. It has a buy book and a sell book, where each side of the book contains a bunch of price levels, and each price level contains a list of orders (first in first out).

# Example of Price Levels and Queued Quantity:

|Price|Quantity|
|---|---|
|100.13|100|
|100.12|600|
|100.11|900|
|100.10|200|
|100.08|500|
|100.07|100|
|100.06|1100|
|100.05|500|

# What Happens When Placing a Market Order to Buy 2700 Shares?

The buy order is matched with all the sell orders at price 100.10, and the first order at price 100.11 (illustrated in light red).
---
#

# Order Book Data Structure

# Order Book Data Structure

When dealing with an order book, it is essential to have an efficient data structure that meets certain criteria:

Criteria
Description

Constant Lookup Time
Operations should include getting volume at a price level or between price levels, and querying the best bid/ask with constant lookup time.

Fast Operations
Add/cancel/execute/update operations should be fast, preferably with O(1) time complexity. These operations involve placing a new order, canceling an order, and matching an order.

Having an efficient data structure for an order book ensures smooth trading processes and accurate price discovery.
---
#

# Stock Exchange Design

# Stock Exchange Design

The stock market has been volatile recently. Coincidentally, we just finished a new chapter "Design a stock exchange". I'll use plain English to explain what happens when you place a stock buying order. The focus is on the exchange side.

|Stock Exchange|Data Service|Market Data Publisher|Client|
|---|---|---|---|
|candlestick chart; order book|Aggregated Risk Check|Order Matching Engine|Order Manager|
|Broker Gateway|Sequencer|Order Book|Wallet|
|Robinhood; MorganStanley|Reporter DB|orders; trades| |

# Steps:

1. Client places an order via the broker's web or mobile app.
2. Broker sends the order to the exchange.

151
---
#

# Stock Exchange Operations

# Stock Exchange Operations

Below are the steps involved in the operation of a stock exchange:

Step
Description

Step 3
The exchange client gateway performs operations such as validation, rate limiting, authentication, normalization, etc, and sends the order to the order manager.

Step 4
The order manager performs risk checks based on rules set by the risk manager.

Step 5
Once risk checks pass, the order manager checks if there is enough balance in the wallet.

Step 6-7
The order is sent to the matching engine. The matching engine sends back the execution result if a match is found. Both order and execution results need to be sequenced first in the sequencer so that matching determinism is guaranteed.

Step 8 - 10
Execution result is passed all the way back to the client.

Step 11-12
Market data (including the candlestick chart and order book) are sent to the data service for consolidation. Brokers query the data service to get the market data.

Step 13
The reporter composes all the necessary reporting fields (e.g. client_id, price, quantity, order_type, filled_quantity, remaining_quantity) and writes the data to the database for persistence.

A stock exchange requires extremely low latency. While most web applications are ok with hundreds of milliseconds latency, a stock exchange requires micro-second level latency.

I’ll leave the latency discussion for a separate post since the post is already long.

Reference: 152
---
#

# Payment System Design

# Design a Payment System

Today is Cyber Monday. Here is how money moves when you click the Buy button on Amazon or any of your favorite shopping websites.

Payment Event
Payment Service
Payment Order
Payment Executor

PayPal
VISA
Stripe
Mastercard

Ledger
Wallet
Payment System
Providers (PSP)

1. When a user clicks the “Buy” button, a payment event is generated and sent to the payment service.
2. The payment service stores the payment event in the database.
3. Sometimes a single payment event may contain several payment orders. For example, you may select products from multiple sellers in a single checkout process. The payment service will call the payment executor for each payment order.
4. The payment executor stores the payment order in the database.
5. The payment executor calls an external PSP to finish the credit card payment.
6. After the payment executor has successfully executed the payment, the payment service will update the wallet to record how much money a given seller has.

Reference: Diagram and steps provided for understanding the payment system design.
---
#

# Transaction Process

# Transaction Process

Step
Description

7
The wallet server stores the updated balance information in the database.

8
After the wallet service has successfully updated the seller’s balance information, the payment service will call the ledger to update it.

9
The ledger service appends the new ledger information to the database.

10
Every night the PSP or banks send settlement files to their clients. The settlement file contains the balance of the bank account, together with all the transactions that took place on this bank account during the day.
---
#

# Flash Sale System Design

# Design a Flash Sale System

# Product Design:

Use reCaptcha before placing an order to prevent bots for suspicious activities.

# Frontend Design:

- Less web page elements
- Less JavaScript loading
- Static contents in CDN

# Over Sale Prevention:

- Lock the inventory when placing an order to decrease the inventory after payment is successful

# Backend Service Design:

- Isolated instance for Black Friday
- Use message queue for asynchronous processing
- Less RPC, less dependencies on other services
- No single point of failure

# Design Principles:

1. Less is more - fewer elements on the web page, fewer data queries, fewer web requests, fewer system dependencies
2. Short critical path - fewer hops among services or merge into one service
3. Async - use message queues to handle high TPS
4. Isolation - isolate static and dynamic contents, isolate processes and databases for rare items
5. Overselling is bad - Decreasing the inventory is important
---
#
# User Experience Importance

6. Why is user experience important?

We definitely don’t want to inform users that they have successfully placed orders but later tell them no items are actually available.
---
#

# Back-of-the-envelope estimation

# Back-of-the-envelope estimation

Recently, a few engineers asked me whether we really need back-of-the-envelope estimation in a system design interview. I think it would be helpful to clarify.

Estimations are important because we need them to understand the scale of the system and justify the design. It helps answer questions like:

- Do we really need a distributed solution?
- Is a cache layer necessary?
- Shall we choose data replication or sharding?

Here is an example of how the estimations shape the design decision.

One interview question is to design proximity service and how to scale geospatial index is a key part of it. Here are a few paragraphs we wrote to show why jumping to a sharding design without estimations is a bad idea:

One common mistake about scaling the geospatial index is to quickly jump to a sharding scheme without considering the actual data size of the table. In our case, the full dataset for the geospatial index table is not large (quadtree index only takes 1.71G memory and storage requirement for geohash index is similar). The whole geospatial index can easily fit in the working set of a modern database server. However, depending on the read volume, a single database server might not have enough CPU or network bandwidth to service all read requests. If that is the case, it will be necessary to spread the read load among multiple database servers.

There are two general approaches to spread the load of a relational database server. We can add read replicas or shard the database.

Many engineers like to talk about sharding during interviews. However, it might not be a good fit for the geohash table. Sharding is complicated. The sharding logic has to be added to the application layer. Sometimes, sharding is the only option. In this case though, since everything can fit in the working set of a database server, there is no strong technical reason to shard the data among multiple servers.
---
#

# Geospatial Index Table Scaling Recommendation

# Geospatial Index Table Scaling Recommendation

A better approach, in this case, is to have a series of read replicas to help with the read load. This method is much simpler to develop and maintain. Thus, we recommend scaling the geospatial index table through replicas.

Check out our bestselling system design books:

|Paperback:|Amazon|
|---|---|
|Digital:|ByteByteGo|

158
#

# Sandeep Raj's Resume

# Sandeep Raj's Resume

# Contact Information

Portfolio: sandy7970

Email: sandeeprajvit@gmail.com

Mobile: +91-797-0573-757

Github: Sandeep-Raj-cse

Linkedin: sandeep-raj

# Experience

|Position|Company|Location|Duration|
|---|---|---|---|
|Software Developer (Internship)|Visteon|Bengaluru|Jan 2024 - June 2024|
|Software Developer (Internship)|Ethnus Codemithra|Remote|May 2023 - July 2023|
|Technical Mentor (Part-time)|MATRIX|Vellore|Aug 2021 - Dec 2022|

# Projects

|Project|Description|Duration|Status|
|---|---|---|---|
|VEHICLE SELLING|Full-Stack web app for vehicle purchases|May 2023 - July 2023|Live - github|
|Gmini|State Management and User Experience app|March 2024 - April 2024|Live - github|
|Pharmacy Management|Web app for doctor-patient scheduling|Aug 2022 - Nov 2022|github|

# Achievements

1. 650+ Questions at Leetcode. Ranked under Top 22.19 percent among all with Highest rating of 1607.
2. 3* at Codechef with 1637 max and 1135 at Codeforces.
3. Secured Global rank 3366 in Mega Job-A-Thon by GFG and 4612 Rank on Leetcode.
4. Solved more than 1100+ problems across platforms.
5. Ranked 5th on GFG (500+) in VIT University.

# Technical Skills

- Programming Language: C++, Java
- Frontend: HTML, CSS, JavaScript, ReactJS, Tailwind, GSAP, EJS
- Backend: MongoDB, NodeJS, SQL, Express

# Coding Profiles

- Leetcode: sandy-7970
- GeeksForGeeks: sandeep-raj-vit
- Codeforces: sandy-79
- Codechef: sandy-79

# Education

B.Tech in Computer Science and Engineering

Vellore Institute of Technology, Vellore, Tamil Nadu, India

Aug 2020 - July 2024

Courses: Operating Systems, Data Structures, Analysis Of Algorithms, Artificial Intelligence, OOPS, Networking, Databases
#
# OCR Text

SQLby
APNA
COLLEGE
---
#
# Database Quiz

# Database Quiz

Question 1: What is a database?
a) A collection of data in a format pat can be easily accessed (Digital)
b) A collection of physical files
c) A collection of images
d) A collection of videos

Question 2: What is pe software application used to manage a database?
a) DBMS (Database Management System)
b) Photoshop
c) Microsoft Word
d) Excel
---
#

# Types of Databases

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|SQLServer| |
|Microsoft| |
|MySQL| |
|ORACLE|PostgreSQL|
|We use SQL to work with relational DBMS|APNA COLLEGE|
---
#
# SQL

# Question:

What is SQL?

# Answer:

Structured Query Language

SQL is a programming language used to interact with relational databases.

It is used to perform CRUD operations:

CRUD Operations
Create
Read
Update
Delete

APNA COLLEGE
---
#

# Database Structure

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#
# Table Example

# Student Table

RollNo
Name
Class
DOB
Gender
City
Marks

1
Nanda
X
1995-06-06
Female
Agra
551

2
Saurabh
XII
1993-05-07

Mumbai
462

3
Sonal
XI
1994-05-06

Delhi
400

4
Trisla
XII
1995-08-08

Mumbai
450

5
Store
XII
1995-10-08

Delhi
369

6

7
Marisla Neha
XI
1995-12-08

Hoscou Dubai
250 377

8
Nishant
X
1995-06-12
Male
Hoscou
489

APNA COLLEGE
---
#

# SQL Queries

# Creating our First Database

Our first SQL Query

SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#
# Creating our First Table

# Creating our First Table

USE db_name;

CREATE TABLE student

id
name
age

INT PRIMARY KEY
VARCHAR(50)
INT NOT NULL

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store X-bit values, X can range from 1 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

# SQL Datatypes

|Datatype|Range|
|---|---|
|TINYINT UNSIGNED|0 to 255|
|TINYINT|-128 to 127|

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

|Query|Description|
|---|---|
|CREATE DATABASE db_name;|Creates a new database with the specified name.|
|CREATE DATABASE IF NOT EXISTS db_name;|Creates a new database with the specified name if it does not already exist.|
|DROP DATABASE db_name;|Drops/deletes the specified database.|
|DROP DATABASE IF EXISTS db_name;|Drops/deletes the specified database if it exists.|
|SHOW DATABASES;|Displays a list of all databases in the system.|
|SHOW TABLES;|Displays a list of all tables in the current database.|
---
#

# Table related Queries

# Table related Queries

# Create Table Syntax:

|Command|Description|
|---|---|
|CREATE TABLE table_name (|Creates a new table with the specified name|
|column_name1 datatype constraint,|Defines the first column with its data type and constraint|
|column_name2 datatype constraint,|Defines the second column with its data type and constraint|

# Example:

CREATE TABLE student (

&nbsp;&nbsp;rollno INT PRIMARY KEY,

&nbsp;&nbsp;name VARCHAR(50)

);

APNA COLLEGE
---
#
# Table related Queries

# Table related Queries

Select & View ALL columns

SELECT * FROM table_name;
SELECTX FROM student;

APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

# Insert Query Example:

Below is an example of an INSERT query:

table_name
colname1
colname2

INSERT INTO table_name
(col1_v1, col2_v1)
(col1_v2, col2_v2)

# Example:

INSERT INTO student (rollno, name) VALUES (101, "arjun");

INSERT INTO student (rollno, name) VALUES (102, "karan");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

# Keys

# Keys

table1 - Student

id
name
cityId
city

101
karan

Pune

102
arjun

Mumbai

103
ram
3
Pune

104
shyam3
HULL
Delhi

NULL
HULL
NULL
HULL

table2 - City

id
city_name

Pune

Mumbai

3
Delhi

HULL
HULL

APNA COLLEGE
---
|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in the column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique and not null, used only for one|id int PRIMARY KEY|
---
|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables. Example: CREATE TABLE temp ( &emsp; cust_id int, &emsp; FOREIGN KEY (cust_id) REFERENCES customer(id) ); |
|DEFAULT|Sets the default value of a column. Example: salary INT DEFAULT 25000 Default value for salary column is set to 25000.|
---
#
# Constraints

# Constraints

Constraints in a database can limit the values allowed in a column.

|Table Name|Columns|Constraints|
|---|---|---|
|city|age INT, city INT, id INT VARCHAR(50)|- CONSTRAINT age_check CHECK (age >= 18 AND city = "Delhi")
- CONSTRAINT age CHECK (age >= 18 AND city = "Delhi")
|
|newTab|age INT|CONSTRAINT CHECK (age >= 18)|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|Query|Description|
|---|---|
|CREATE DATABASE college;|Creates a database named college|
|USE college;|Switches to the college database|
|CREATE TABLE student|Creates a table named student|
|INSERT INTO student (rollno, name, marks, grade, city) VALUES|Inserts data into the student table|

# Inserted Data

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|

# APNA COLLEGE
---
#
# Select in Detail

# SELECT in Detail

Used to select any data from the database

# Basic Syntax

SELECT col1, col2 FROM table_name;

# To Select ALL

SELECT * FROM table_name;

# APNA COLLEGE
---
#
# Where Clause

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT x FROM student WHERE marks > 80;|Marks greater than 80|
|SELECT * FROM student WHERE city = "Mumbai";|City is Mumbai|

APNA COLLEGE
---
#
# Where Clause

# Using Operators in WHERE

Arithmetic Operators: + (addition), - (subtraction), * (multiplication), / (division), % (modulus)

Comparison Operators: = (equal to), != (not equal to), >, >=, <, <=

Logical Operators: AND, OR, NOT, IN, BETWEEN, ALL, LIKE, ANY

Bitwise Operators: & (Bitwise AND), | (Bitwise OR)
---
#

# Operators

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT X FROM student WHERE marks > 80 AND city = "Mumbai"|
|OR|To check for one of the conditions to be true|SELECT X FROM student WHERE marks > 90 OR city = "Mumbai"|

APNA COLLEGE
---
#

# Operators

# Operators

Operator
Description

BETWEEN
Selects for a given range

SELECT * FROM student WHERE marks BETWEEN 80 AND 90;

IN
Matches any value in the list

SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai');

NOT
To negate the given condition

SELECT * FROM student WHERE city NOT IN ('Delhi', 'APNA', 'Mumbai');
---
#
# Limit Clause

# Limit Clause

Sets an upper limit on the number of rows to be returned.

Query Syntax
SELECT column_name FROM table_name LIMIT number;

Example:

SELECT col1, col2 FROM table_name LIMIT 3;

Explanation:

This query will return the values of col1 and col2 from the table_name but will limit the result to only 3 rows.
---
#
# Order By Clause

# Order By Clause

To sort in ascending (ASC) or descending order (DESC):

|Query|Description|
|---|---|
|SELECT * FROM student ORDER BY city ASC;|Sort all records from the 'student' table by the 'city' column in ascending order.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Select specific columns 'col1' and 'col2' from 'table_name' and sort the results by column 'col_name(s)' in ascending order.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Aggregate functions perform a calculation on a set of values, and return a single value.

Function
Description

COUNT( )
Counts the number of rows

MAX( )
Returns the maximum value

MIN( )
Returns the minimum value

SUM( )
Calculates the sum of values

AVG( )
Calculates the average value

Example:

Get Maximum Marks

SELECT MAX(marks)
FROM student;

Get Average marks

SELECT AVG(marks)
FROM student;

APNA COLLEGE
---
#
# Group By Clause

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally we use group by with some aggregation function.

# Example: Count number of students in each city

|city|count(name)|
|---|---|
|APNA COLLEGE|SELECT city, count(name) FROM student GROUP BY city;|
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

City
Number of Students

City Name
Count

Example City
25

Another City
18

SQL Query:

SELECT COUNT(name) AS Number_of_Students, city
FROM student
GROUP BY city
HAVING MAX(marks) > 90;

APNA COLLEGE
---
#
# General Order Query

# General Order Query

Below is the syntax for a general order query in SQL:

SELECT column(s)
FROM table_name
WHERE condition
GROUP BY column(s)
HAVING condition
ORDER BY column(s) ASC;

# APNA COLLEGE
---
#
# Having Clause

# Having Clause

Similar to the Where clause, the Having clause applies some condition on rows. It is used when we want to apply any condition after grouping.

Count the number of students in each city where the maximum marks cross 90.

City
Number of Students

New York
15

Los Angeles
10

Chicago
8
---
#

# Table related Queries

# Table related Queries

# Update Query Syntax:

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
This query is used to update existing rows in a table by setting new values for specified columns based on a condition.

# Example:

Update the grade of students from "A" to "0" in the student table:

UPDATE student
SET grade = "0"
WHERE grade = "A";

APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query to delete existing rows from a table:

SQL Query
Description

DELETE FROM table_name WHERE condition;
This query deletes rows from the specified table based on the specified condition.

DELETE FROM student WHERE marks = 33;
This specific query deletes rows from the 'student' table where the 'marks' column has a value of 33.

Example:

DELETE FROM student
WHERE marks = 33;

APNA COLLEGE
---
#

# Foreign Key Cascading

# Foreign Key Cascading

When working with foreign keys, we can specify cascading actions to maintain referential integrity. Two common options are:

Cascade Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table.

Example:

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

In the above example, the courseID column in the student table is a foreign key referencing the id column in the course table. The cascading actions are set to delete or update the referencing rows in the student table based on the actions performed on the parent table.

APNA COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Syntax

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#
# Table Related Queries

# CHANGE Column (rename)

|Query|Description|
|---|---|
|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|This query is used to change the name, datatype, and constraint of a column in a table.|

# MODIFY Column (modify datatype/constraint)

|Query|Description|
|---|---|
|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|This query is used to modify the datatype and constraint of a column in a table.|
---
#

# SQL Commands

# SQL Commands

Operation
SQL Command

ADD Column
ALTER TABLE student ADD COLUMN age INT NOT NULL DEFAULT 19;

DROP Column
ALTER TABLE student DROP COLUMN stu_age;

MODIFY Column
ALTER TABLE student MODIFY age VARCHAR(2);

RENAME Table
ALTER TABLE student RENAME TO stu;

CHANGE Column (rename)
ALTER TABLE student CHANGE age stu_age INT;

Note: The commands above are SQL commands for modifying tables in a database.
---
#
# Table related Queries

# Table related Queries

Truncate (to delete table's data)

TRUNCATE TABLE table_name;
UPDATE student
SET grade = "0"
WHERE grade = "A"

APNA COLLEGE
---
#
# Joins in SQL

# Joins in SQL

Join is used to combine rows from two or more tables, based on a related column between them.

APNA
COLLEGE
---
#

# Types of Joins

# Types of Joins

Join Type
Description

Inner Join
Combines rows from two tables based on a matching condition

Left Join
Returns all rows from the left table and the matched rows from the right table

Right Join
Returns all rows from the right table and the matched rows from the left table

Full Join
Returns all rows when there is a match in either the left or right table
---
#
# Inner Join

# Inner Join

Inner Join returns records that have matching values in both tables.

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# SQL Inner Join Example

# SQL Inner Join Example

student_id
name
course

102

103
casey
science

bob
english

APNA COLLEGE
---
#
# Left Join

# Left Join

Returns all records from the left table, and the matched records from the right table.

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

student_id
name
course

101
adam
null

102
bob
english

103
casey
science

Result:

student_id
name
course

101
adam
APNA

102
bob
english

103
casey
COLLEGE
---
#

# Right Join

# Right Join

Right Join returns all records from the right table, and the matched records from the left table.

LEFT INCLUSIVE
LEFT EXCLUSIVE
RIGHT INCLUSIVE
RIGHT EXCLUSIVE

Right Join
FULL OUTER INCLUSIVE
INNER JOIN
FULL OUTER EXCLUSIVE

# Syntax

SELECT column(s)

FROM tableA

RIGHT JOIN tableB

ON tableA.col_name = tableB.col_name;

APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student_id
course
name

102
english
bob

105

103
science

math
null

casey

107
computer science
null
---
Full Join
Returns all records when pere is a match in eiper left or right table

Syntax in MySQL
SELECT * FROM student as a LEFT JOIN course as b ON a.id = b.id UNION SELECT * FROM student as a RIGHT JOIN course as b ON a.id = b.id;
---
#

# Full Join Example

# Full Join Example

student_id
name
course

101
adam
null

102
bob
english

103

105
casey
null

null
science

null
math

107
null
computer science
---
#

# Think & Ans

LEFT EXCLUSIVE
RIGHT INCLUSIVE
RIGHT EXCLUSIVE

Qs:LEFT EXCLUSIVE
Write SQL commands to display the right exclusive join :
RIGHT EXCLUSIVE

FULL OUTER INCLUSIVE
INNER JOIN
FULL OUTER EXCLUSIVE

INNER JOIN
LEFT EXCLUSIVE Join
Right Exclusive Join

|SELECT|FROM|AS|WHERE|
|---|---|---|---|
|X|student|a|ON a.id = b.id WHERE b.id IS NULL;|
|APNA|COLLEGE| | |
---
#
# Self Join

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

APNA COLLEGE
---
#

# Self Join Example

# Self Join Example

manager_name
name

adam
casey

donald
casey

Result:

APNA COLLEGE
---
#

# Union Operator

# Union Operator

The UNION operator is used to combine the result-set of two or more SELECT statements and returns only unique records.

# Usage:

- Every SELECT statement should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT statement should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

Example:

SELECT name FROM employees

UNION

SELECT name FROM contractors;

APNA COLLEGE
---
#

# SQL Sub Queries

# SQL Sub Queries

A Subquery or Inner query or a Nested query is a query within another SQL query.

|Query Syntax|Sub Query|
|---|---|
|SELECT column(s) FROM table_name WHERE col_name operator ( subquery ); |APNA COLLEGE |
---
#
# SQL Sub Queries

# SQL Sub Queries

Roll No
Name
Marks
City

102
bhumika
93
Mumbai

103
chetan
85
Mumbai

104
dhruv
96
Delhi

105
emanuel
92
Delhi

106
farah
82
Delhi

Step 1. Find the average of the class

Step 2. Find the names of students with marks greater than the class average
---
#
# SQL Sub Queries

# Example: Find the names of all students with even roll numbers

Step
Description

Step 1
Find the even roll numbers

Step 2
Find the names of students with even roll numbers

# APNA COLLEGE
---
#
# SQL Sub Queries

# Example with FROM

Find the max marks from the students of Delhi

Step 1
Find the students of Mumbai

Step 2
Find their max marks using the sublist in step 1

# APNA COLLEGE
---
#
# MySQL Views

# MySQL Views

A view is a virtual table based on the result-set of an SQL statement.

SQL Statement to Create a View:
CREATE VIEW view1 AS SELECT rollNo, name FROM student;

To select data from the view:

SELECT * FROM view1;

A view always shows up-to-date data. The database engine recreates the view every time a user queries it.

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is the name of the college?|APNA COLLEGE|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

|Question|Answer|
|---|---|
|What is a database?|A collection of data in a format that can be easily accessed (Digital)|
|What is a software application used to manage a database?|DBMS (Database Management System)|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Types of Databases

|Relational|Non-relational (NoSQL)|
|---|---|
|Data stored in tables|Data not stored in tables|
|- SQL Server
- MySQL
- ORACLE
- PostgreSQL
|APNA COLLEGE|
|We use SQL to work with relational DBMS| |
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Question:

What is SQL?

# Answer:

Structured Query Language
SQL is a programming language used to interact wip relational databases.
It is used to perform CRUD operations:

- Create
- Read
- Update
- Delete
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Database Structure

|Database|
|---|
|Table 1|Table 2|
|Data|Data|
|APNA COLLEGE|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Student Table

|RollNo|Name|Class|DOB|Gender|City|Marks|
|---|---|---|---|---|---|---|
|1|Nanda|X|1995-06-06|1|Agra|551|
|2|Saurabh|XII|1993-05-07| |Mumbai|462|
|5|Sonal|XI|1994-05-06| |Delhi|400|
| |Stosea|XII|1995-88-08| |Dumbai|369|
|6|Marisla|XI|1994-12-12| |Dubai|250|
| |Neha|X|1995-12-08| |Moscou|377|
|8|Nishant|X|1995-06-12| |Hoscou|489|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Creating our First Database

Our first SQL Query
CREATE DATABASE db_name;
DROP DATABASE db_name;

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Creating our First Table

|USE db_name;|CREATE TABLE student|
|---|---|
| |id INT PRIMARY KEY,|
|CREATE TABLE table_name (|name VARCHAR(50)|
|column_name1 datatype constraint,|age INT NOT NULL|
|column_name2 datatype constraint,| |
|column_name2 datatype constraint| |

# APNA COLLEGE
---
#

# SQL Datatypes

# SQL Datatypes

DATATYPE
DESCRIPTION
USAGE

CHAR
string(0-255), can store characters of fixed length
CHAR(50)

VARCHAR
string(0-255), can store characters up to given length
VARCHAR(50)

BLOB
string(0-65535), can store binary large object
BLOB(1000)

INT
integer(-2,147,483,648 to 2,147,483,647)
INT

TINYINT
integer(-128 to 127)
TINYINT

BIGINT
integer(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
BIGINT

BIT
can store -bit values: X can range from 0 to 64
BIT(2)

FLOAT
Decimal number with precision to 23 digits
FLOAT

DOUBLE
Decimal number with 24 to 53 digits
DOUBLE

BOOLEAN
Boolean values 0 or 1
BOOLEAN

DATE
date in format of YYYY-MM-DD ranging from 1000-01-01 to 9999-12-31
DATE

YEAR
year in 4 digits format ranging from 1901 to 2155
YEAR
---
#

# SQL Datatypes

Datatype
Range

TINYINT UNSIGNED
0 to 255

TINYINT
-128 to 127

APNA COLLEGE
---
#

# Types of SQL Commands

# Types of SQL Commands

Category
Commands

DDL (Data Definition Language)
create, alter, rename, truncate, drop

DQL (Data Query Language)
select

DML (Data Manipulation Language)
select, insert, update, delete

DCL (Data Control Language)
grant, revoke permission to users

TCL (Transaction Control Language)
start transaction, commit, rollback etc.
---
#

# Database related Queries

# Database related Queries

Queries
CREATE DATABASE db_name;
CREATE DATABASE IF NOT EXISTS db_name;
CREATEDATABASEIFNOT EXISTS college;
DROP DATABASE db_name;
DROP DATABASE IF EXISTS db_name;
SHOW DATABASES;
SHOW TABLES;
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Table related Queries

Create

CREATE TABLE table_name (

column_name1 datatype constraint,

column_name2 datatype constraint

);

CREATETABLE student

rollno INT PRIMARY KEY 1

name VARCHAR(50)

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

SELECT * FROM table_name;
SELECT * FROM student;
APNA
COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

Insert
INSERT INTO table_name (colname1, colname2); VALUES (col1_v1, col2_v1), (col1_v2, col2_v2);

Example
INSERT INTO student (rollno, name) VALUES (101, "karan"), (102, "arjun");

APNA COLLEGE
---
#

# Keys in Database

# Keys

Key Type
Description

Primary Key
It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id) There is only 1 PK & it should be NOT null.

Foreign Key
A foreign key is a column (or set of columns) in a table that refers to the primary key in another table. There can be multiple FKs. FKs can have duplicate & null values.
---
#

table {
width: 50%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Student Table

|id|name|cityId|city|
|---|---|---|---|
|101|karan| |Pune|
|102|arjun| |Mumbai|
|103|ram| |Pune|
|104|shyam3| |Delhi|

# City Table

|id|city_name|
|---|---|
| |Pune|
| |Mumbai|
| |Delhi|
|NULL|HULL|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: left;
}

# Constraints

|Constraint|Description|Example|
|---|---|---|
|NOT NULL|Columns cannot have a null value|col1 int NOT NULL|
|UNIQUE|All values in column are different|col2 int UNIQUE|
|PRIMARY KEY|Makes a column unique & not null but used only for one|id int PRIMARY KEY|

Example of creating a table with constraints:

CREATE TABLE temp
id int not null,
PRIMARY KEY (id)
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Constraints

|Constraint|Description|
|---|---|
|FOREIGN KEY|Prevents actions that would destroy links between tables|
|DEFAULT|Sets the default value of a column|

# Example:

|SQL Query|Description|
|---|---|
|CREATE TABLE temp ( cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(id) )|Creates a table 'temp' with a foreign key constraint linking 'cust_id' to 'customer(id)'|
|salary INT DEFAULT 25000|Sets the default value of 'salary' column to 25000|
---
|Constraints|
|---|
|<br/>CHECK|it can limit the values allowed in a column|
|CREATE TABLE city| |
|id INT PRIMARY KEY| |
|city VARCHAR (50)| |
|age INT| |
|CONSTRAINT age CHECK (age >= 18 AND city = 'Delhi')| |
|CREATE TABLE newTab| |
|age INT CHECK (age >= 18)| |

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 8px;
text-align: left;
}

# Sample Table

|rollno|name|marks|grade|city|
|---|---|---|---|---|
|101|anil|78|C|Pune|
|102|bhumika|93|A|Mumbai|
|103|chetan|85|B|Mumbai|
|104|dhruv|96|A|Delhi|
|105|emanuel|12|F|Delhi|
|106|farah|82|B|Delhi|
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Select in Detail

|Description|SQL Syntax|
|---|---|
|Used to select any data from the database|SELECT col1, col2 FROM table_name;|

# To Select ALL

SQL Syntax
SELECT * FROM table_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

To define some conditions

|SQL Query|Conditions|
|---|---|
|SELECT col1, col2 FROM table_name WHERE conditions;| |
|SELECT * FROM student WHERE marks=780;|Marks equal to 780|
|SELECT * FROM student WHERE city="Mumbai";|City is Mumbai|

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Where Clause

|Arithmetic Operators|Description|
|---|---|
|+|Addition|
|-|Subtraction|
|*|Multiplication|
|/|Division|
|%|Modulus|

|Comparison Operators|Description|
|---|---|
|=|Equal to|
|!=|Not equal to|
|&gt;|Greater than|
|&gt;=|Greater than or equal to|
|&lt;|Less than|
|&lt;=|Less than or equal to|

|Logical Operators|Description|
|---|---|
|AND|Logical AND|
|OR|Logical OR|
|NOT|Logical NOT|
|IN|IN Operator|
|BETWEEN|BETWEEN Operator|
|LIKE|LIKE Operator|
|ANY|ANY Operator|

|Bitwise Operators|Description|
|---|---|
|&|Bitwise AND|
|||Bitwise OR|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|AND|To check for both conditions to be true|SELECT FROM student WHERE marks > 80 AND city = "Mumbai";|
|OR|To check for one of the conditions to be true|SELECT FROM student WHERE marks > 90 OR city = "Mumbai";|

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Operators

|Operator|Description|Example|
|---|---|---|
|BETWEEN|Selects for a given range|SELECT * FROM student WHERE marks BETWEEN 80 AND 90|
|IN|Matches any value in the list|SELECT * FROM student WHERE city IN ('Delhi', 'Mumbai')|
|NOT|To negate the given condition|SELECT * FROM student WHERE city NOT IN ('Delhi', 'Mumbai')|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Limit Clause

|Description|Example|
|---|---|
|Sets an upper limit on number of (tuples) rows to be returned|SELECT X FROM student LIMIT 3;|
|General Syntax|SELECT col1, col2 FROM table_name LIMIT number;|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Order By Clause

|Query Syntax|Description|
|---|---|
|SELECT X FROM student ORDER BY city ASC;|Sorts the result set in ascending order based on the 'city' column in the 'student' table.|
|SELECT col1, col2 FROM table_name ORDER BY col_name(s) ASC;|Sorts the result set in ascending order based on the specified column(s) in the 'table_name' table.|

# APNA COLLEGE
---
#

# Aggregate Functions

# Aggregate Functions

Function
Description

COUNT( )
Counts the number of rows in a table

MAX( )
Returns the maximum value in a set of values

MIN( )
Returns the minimum value in a set of values

SUM( )
Calculates the sum of a set of values

AVG( )
Calculates the average of a set of values

Example:

Query
Description

SELECT avg(marks) FROM student;
Get Average marks from the student table

SELECT max(marks) FROM student;
Get Maximum Marks from the student table
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Group By Clause

Groups rows that have the same values into summary rows. It collects data from multiple records and groups the result by one or more columns.

Generally, we use GROUP BY with some aggregation function.

|SQL Query|Description|
|---|---|
|SELECT city, COUNT(name) FROM student GROUP BY city;|Count number of students in each city|

APNA COLLEGE
---
#

# Having Clause

# Having Clause

Similar to WHERE clause, HAVING clause applies some condition on rows. It is used when we want to apply any condition after grouping.

# Count number of students in each city where max marks cross 90:

SELECT count(name), city
FROM student
GROUP BY city
HAVING max(marks) > 90;

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# General Order Query Syntax

|Keyword|Description|
|---|---|
|SELECT column(s)|Specifies the columns to retrieve data from|
|FROM table_name|Specifies the table from which to retrieve data|
|WHERE condition|Specifies the condition to filter rows|
|GROUP BY column(s)|Groups the result set by the specified column(s)|
|HAVING condition|Filters groups based on the specified condition|
|ORDER BY column(s) ASC|Orders the result set in ascending order based on the specified column(s)|

# APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Having Clause

|Concept|Similar to WHERE clause, applies some condition on rows.|
|---|---|
|Usage|Used when we want to apply any condition after grouping.|
|Example|Count number of students in each city where max marks cross 90.|

# APNA COLLEGE
---
#

# Table related Queries

# Table related Queries

Query
Description

UPDATE table_name SET col1 = val1, col2 = val2 WHERE condition;
Update existing rows in a table by setting the values of specified columns based on a condition.

UPDATE student SET grade = "0" WHERE grade = "A";
Update the 'grade' column in the 'student' table, setting the value to "0" where the current grade is "A".

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

Delete (to delete existing rows)

|Query|Description|
|---|---|
|DELETE FROM table_name WHERE condition;|Delete rows from a table based on a specified condition.|
|DELETE FROM student WHERE marks = 33;|Delete rows from the 'student' table where the 'marks' column equals 33.|
---
#

# Foreign Key Cascading

# Foreign Key Cascading Options

Cascading Type
Description

On Delete Cascade
Deletes the referencing rows in the child table when the referenced row is deleted in the parent table with a primary key.

On Update Cascade
Updates the referencing rows in the child table when the referenced row is updated in the parent table with a primary key.

# Example SQL Table Creation with Cascading

Table Name: student

CREATE TABLE student (
id INT PRIMARY KEY,
courseID INT,
FOREIGN KEY (courseID) REFERENCES course(id) ON DELETE CASCADE ON UPDATE CASCADE
);

COLLEGE
---
#

# Table Related Queries

# Table Related Queries

Query
Description

ADD Column
ALTER TABLE table_name ADD COLUMN column_name datatype constraint;

DROP Column
ALTER TABLE table_name DROP COLUMN column_name;

RENAME Table
ALTER TABLE table_name RENAME TO new_table_name;
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table Related Queries

|Query|Description|
|---|---|
|CHANGE Column (rename)|ALTER TABLE table_name CHANGE COLUMN old_name new_name new_datatype new_constraint;|
|MODIFY Column (modify datatype/constraint)|ALTER TABLE table_name MODIFY col_name new_datatype new_constraint;|
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Commands

|Operation|Table|Column|Details|
|---|---|---|---|
|ADD Column|ALTER TABLE student| |ADD COLUMN age INT NOT NULL DEFAULT 19;|
|DROP Column|ALTER TABLE student| |DROP COLUMN stu_age;|
|MODIFY Column|ALTER TABLE student| |MODIFY age VARCHAR(2);|
|RENAME Table|ALTER TABLE student| |RENAME TO stu;|
|CHANGE Column (rename)|ALTER TABLE student|age|CHANGE age stu_age INT;|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Table related Queries

|Query|Description|
|---|---|
|TRUNCATE TABLE table_name;|Deletes all data in the specified table.|
|UPDATE student SET grade="0" WHERE grade="A";|Updates the grade to "0" for students who currently have a grade of "A".|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}

table, th, td {
border: 1px solid black;
}

th, td {
padding: 10px;
text-align: left;
}

# Joins in SQL

Definition
Join is used to combine rows from two or more tables, based on a related column between them.
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# Types of Joins

|Join Type|Description|
|---|---|
|Left Inclusive|Includes all records from the left table and matching records from the right table|
|Inner Join|Returns records that have matching values in both tables|
|Full Outer Exclusive|Includes all records when there is a match in either left or right table, but not both|
|Left Exclusive|Includes all records from the left table that do not have a match in the right table|
|Right Inclusive|Includes all records from the right table and matching records from the left table|
|Full Outer Inclusive|Includes all records when there is a match in either left or right table, or both|
|Right Exclusive|Includes all records from the right table that do not have a match in the left table|

# Outer Joins

|Join Type|Description|
|---|---|
|Left Join|Returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.|
|Right Join|Returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.|
|Full Join|Returns all records when there is a match in either left or right table, or both. If there is no match, the result is NULL on the unmatched side.|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Inner Join

Returns records that have matching values in both tables

# Syntax:

SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Query and Result

SELECT *
Inner Join
FROM student
INNER JOIN course
ON student.student_id = course.student_id;

# Student Table

|student_id|name|
|---|---|
|101|adam|
|102|bob|
|103|casey|

# Course Table

|student_id|course|
|---|---|
|102|english|
|105|math|
|103|science|
|107|computer science|

# Result

|student_id|name|course|
|---|---|---|
|102| | |
|103|bob|science|

# College

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Left Join

Returns all records from the left table, and the matched records from the right table

# Syntax:

SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;

# APNA COLLEGE
---
#

# Left Join Example

# Left Join Example

|student|course|
|---|---|
|student_id|name|student_id|course|
|101|adam|102|english|
|102|bob|105|math|
|103|casey|103|science|

Result
student_id
name
course

APNA
101
adam
null

102
bob
english

COLLEGE
103
casey
science
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Right Join

|LEFT INCLUSIVE|LEFT EXCLUSIVE|RIGHT INCLUSIVE|
|---|---|---|
|Returns all records from the right table, and the matched records from the left table| | |

# Syntax

|FULL OUTER INCLUSIVE|INNER JOIN|FULL OUTER EXCLUSIVE|
|---|---|---|
|SELECT column(s) FROM tableA RIGHT JOIN tableB ON tableA.col_name = tableB.col_name;| | |

# APNA COLLEGE
---
#

# Right Join Example

# Right Join Example

student id
course

102
english

105
math

103
science

107
computer science

name
bob
null
casey
null
---
#

# Full Join in MySQL

# Full Join in MySQL

Full Join returns all records when there is a match in either left or right table.

# Syntax in MySQL:

SELECT
FROM student AS a
LEFT JOIN

LEFT JOIN course AS b
UNION
ON a.id = b.id

UNION
SELECT
FROM student AS a

RIGHT JOIN
course AS b
ON a.id = b.id

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Full Join Example

|student id|name|course|
|---|---|---|
|101|adam|null|
|102|bob|english|
|103| | |
|105|casey|null|
| |null|science|
| |null|math|
|107|null|computer science|
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Think & Ans

|LEFT INCLUSIVE|LEFT EXCLUSIVE|
|---|---|
|INNER JOIN|LEFT JOIN|

|RIGHT INCLUSIVE|RIGHT EXCLUSIVE|
|---|---|
|INNER JOIN|RIGHT JOIN|

|FULL OUTER INCLUSIVE|FULL OUTER EXCLUSIVE|
|---|---|
|INNER JOIN|FULL OUTER JOIN|

SELECT * FROM student as a

LEFT JOIN course as b

WHERE a.id = b.id AND b.id IS NULL;

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

th, td {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Self Join

It is a regular join but the table is joined with itself.

# Syntax:

SELECT column(s)
FROM table as a
JOIN table as b
ON a.col_name = b.col_name;

Example:

|EmployeeID|EmployeeName|ManagerID|
|---|---|---|
|1|John|3|
|2|Alice|3|
|3|Bob|NULL|
---
#

# Self Join Example

# Self Join Example

id
name
manager_id

101
adam
103

102
bob
104

103
casey
null

104
donald
103

Result:

manager_name
name

casey
adam

casey
donald
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# Union

It is used to combine the result-set of two or more SELECT statements.

Gives UNIQUE records.

# To use it:

- Every SELECT should have the same number of columns.
- Columns must have similar data types.
- Columns in every SELECT should be in the same order.

# Syntax:

SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB

APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# SQL Sub Queries

|Sub Query|Query|
|---|---|
|A Subquery or Inner query or a Nested query is a query within another SQL query. It involves 2 select statements.|Syntax SELECT column(s) FROM table_name WHERE col_name operator ( subquery );|

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|rollno|name|marks|city|
|---|---|---|---|
|101|anil|78|Pune|
|102|bhumika|93|Mumbai|
|103|chetan|85|Mumbai|
|104|dhruv|96|Delhi|
|105|emanuel|92|Delhi|
|106|farah|82|Delhi|

Get names of all students who scored more than class average.

Step 1. Find the avg of class

Step 2. Find the names of students with marks &gt; avg

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step 1|Find the even roll numbers|
|---|---|
|Step 2|Find the names of students with even roll numbers|

# Example

Find the names of all students with even roll numbers.

APNA COLLEGE
---
#

table {
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 10px;
text-align: left;
}

# SQL Sub Queries

|Step|Description|
|---|---|
|1|Find the students of Mumbai|
|2|Find their max marks using the sublist in step 1|

# Example with FROM

Find the max marks from the students of Delhi

# APNA COLLEGE
---
#

table {
font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
}

td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;
}

th {
background-color: #f2f2f2;
}

# MySQL Views

|Question|Answer|
|---|---|
|What is a view in MySQL?|A view is a virtual table based on the result-set of an SQL statement.|
|How to create a view in MySQL?|CREATE VIEW view1 AS SELECT rollno, name FROM student;|
|How to select data from a view in MySQL?|SELECT X FROM view1;|
|Why is a view useful in MySQL?|A view always shows up-to-date data as the database engine recreates the view every time a user queries it.|

APNA COLLEGE
