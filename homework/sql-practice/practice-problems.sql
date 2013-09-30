-- 2. 

CREATE TABLE person
	(
     id int primary key, 
     name varchar(50), 
     street varchar(25),
     city varchar(25)
    );

CREATE TABLE company
	(
     id int primary key, 
     name varchar(50), 
     city varchar(30)
    );

CREATE TABLE works
	(
     personid int primary key, 
     companyid int, 
     salary int
    );

CREATE TABLE manages
    (
    managerid int,
    employeeid int primary key
    );

-- 3.
-- a. The names of people that work for First Bank Corporation (FBC).

SELECT p.name
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personid
INNER JOIN COMPANY c ON w.companyid = c.id
WHERE c.name = "FBC";

-- b. The names and cities of residence for all FBC employees.

SELECT p.name, p.city
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personid
INNER JOIN COMPANY c ON w.companyid = c.id
WHERE c.name = "FBC";

-- c. The names and addresses of all FBC employees earning under 50K per year.

SELECT p.name,
	   p.street,
	   p.city
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personid
INNER JOIN COMPANY c ON w.companyid = c.id
WHERE c.name = "FBC"
	AND w.salary < 50000;

-- d. All people who live in the same city in which they work.

SELECT person.*
FROM person INNER JOIN works
ON person.id = works.personid
INNER JOIN company
ON person.city = company.city;

-- e. All people who live on the same street and city as their manager.

SELECT *
FROM PERSON INNER JOIN MANAGES
ON

-- f. All people who do not work for FBC.

SELECT *
FROM PERSON INNER JOIN 
	Works
	ON p.id = Works.personID
	AND Works.companyid != 'FBC'


-- g. All people who earn more than every employee of Small Bank Corporation (SBC).
SELECT *
FROM PERSON, WORKS
WHERE  < ALL (SELECT *
					FROM WHERE
					Salary EMPLOYEE Dno=5);

-- h. All companies located in every city in which SBC is located.

-- i. The names of people that work at no company.

SELECT PERSON.name
FROM PERSON
WHERE NOT EXISTS (SELECT * 
				  FROM WORKS)

-- j. All companies that have more than 20 employees.

SELECT COMPANY.name
FROM COMPANY
WHERE (SELECT COUNT(WORKS.companyid)
	   FROM WORKS
	   WHERE WORKS.companyid) > 20












