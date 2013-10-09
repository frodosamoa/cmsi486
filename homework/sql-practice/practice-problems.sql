-- The code below is here: http://sqlfiddle.com/#!2/90357

-- 2. 

CREATE TABLE person (
     id         INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
     name       VARCHAR(50), 
     street     VARCHAR(25),
     city       VARCHAR(25)
);

CREATE TABLE company (
     id         INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
     name       VARCHAR(50), 
     city       VARCHAR(30)
);

CREATE TABLE works (
     personid   INT PRIMARY KEY, 
     companyid  INT, 
     salary     INT,
     FOREIGN KEY (personid) REFERENCES person(id),
     FOREIGN KEY (companyid) REFERENCES company(id)
);

CREATE TABLE manages (
    managerid   INT,
    employeeid  INT PRIMARY KEY
);

-- 3.

-- a. The names of people that work for First Bank Corporation (FBC).

SELECT p.pname
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personid
INNER JOIN COMPANY c ON w.companyid = c.id
WHERE c.cname = "FBC";

-- b. The names and cities of residence for all FBC employees.

SELECT p.pname, p.city
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personid
INNER JOIN COMPANY c ON w.companyid = c.id
WHERE c.cname = "FBC";

-- c. The names and addresses of all FBC employees earning under 50K per year.

SELECT p.pname,
	   p.pstreet,
	   p.pcity
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personid
INNER JOIN COMPANY c ON w.companyid = c.id
WHERE c.cname = "FBC"
	AND w.salary < 50000;

-- d. All people who live in the same city in which they work.

SELECT e.*
FROM PERSON e
INNER JOIN MANAGES ma ON e.id = ma.employeeid
INNER JOIN PERSON m ON m.id = ma.managerid
WHERE e.city = m.city;

-- e. All people who live on the same street and city as their manager.

SELECT e.*
FROM PERSON e
INNER JOIN MANAGES ma ON e.id = ma.employeeid
INNER JOIN PERSON m ON m.id = ma.managerid
WHERE e.pstreet = m.pstreet
	AND e.city = m.city;

-- f. All people who do not work for FBC.

SELECT *
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personID
INNER JOIN COMPANY c ON w.companyid = c.id
WHERE c.cname != 'FBC';

-- g. All people who earn more than every employee of Small Bank Corporation (SBC).

SELECT *
FROM PERSON p
INNER JOIN WORKS w ON p.id = w.personid
WHERE w.salary > ( SELECT MAX(w.salary)
				   FROM WORKS w
				   INNER JOIN COMPANY c ON w.companyid = c.id
				   WHERE c.cname = 'SBC');

-- h. All companies located in every city in which SBC is located.

SELECT c2.cname
FROM COMPANY c1
INNER JOIN COMPANY c2 ON c2.cname != 'SBC'
WHERE c1.ccity = c2.ccity
  AND c1.cname = 'SBC'
  AND c2.cname != 'SBC';

-- i. The names of people that work at no company.

SELECT p.pname
FROM PERSON p
LEFT OUTER JOIN WORKS w ON p.id = w.personid
WHERE w.companyid IS NULL;

-- j. All companies that have more than 20 employees.

SELECT c.cname, COUNT(*) as num_employees
FROM COMPANY c
INNER JOIN WORKS w ON c.id = c.companyid
GROUP by c.cname
HAVING num_employees > 20