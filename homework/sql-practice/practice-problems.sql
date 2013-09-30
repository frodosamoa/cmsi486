-- a. The names of people that work for First Bank Corporation (FBC).

SELECT PERSON.name
FROM PERSON, WORKS, COMPANY
WHERE PERSON.id = WORKS.personid
	  AND COMPANY.name = "FBC";

-- b. The names and cities of residence for all FBC employees.

SELECT person.name, person.ci
FROM person INNER JOIN works
ON person.id = works.personid
INNER JOIN company
ON works.companyid = company.id
WHERE company.name = "FBC";

-- c. The names and addresses of all FBC employees earning under 50K per year.

SELECT p.name, p.street, p.city
FROM person INNER JOIN works
ON works.salary < 50000
INNER JOIN company
ON works.companyid = company.id
WHERE company.name = "FBC";

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












