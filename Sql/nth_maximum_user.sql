create Table employee( no INT, name VARCHAR(50), salary INT);
INSERT into employee values (1,'veer',500),(2,'raaj',1000),(3,'aashu',1300);
SELECT * FROM employee;
SELECT * FROM employee 
ORDER BY salary DESC
LIMIT 1 offset 1;  