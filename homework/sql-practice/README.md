### Practice Problems

1. Here are four relations, representing people and the companies at which they work. People can work at zero or more companies, and can have zero or more managers.

		PERSON(id, name, street, city)
		COMPANY(id, name, city)
		WORKS(personid, companyid, salary)
		MANAGES(managerid, employeeid)

   Draw an EER diagram for these relations and their attributes.

![Problem 1 EER Diagram](http://i.imgur.com/eZrSJo5.png)

2. For the relations in the preceding problem, give SQL DDL to define the relations.

3. For the relations in the preceding problem, give both relational algebra expressions and SQL queries for:
	* The names of people that work for First Bank Corporation (FBC).
	* The names and cities of residence for all FBC employees.
	* The names and addresses of all FBC employees earning under 50K per year.
	* All people who live in the same city in which they work.
	* All people who live on the same street and city as their manager.
	* All people who do not work for FBC.
	* All people who earn more than every employee of Small Bank Corporation (SBC).
	* All companies located in every city in which SBC is located.
	* The names of people that work at no company.
	* All companies that have more than 20 employees.

    [Here](https://github.com/frodosamoa/csmi486/blob/master/homework/sql-practice/practice-problems.sql) are the SQL queries.

4. Give relational calculus expressions for each of the queries in the preceding problem.
