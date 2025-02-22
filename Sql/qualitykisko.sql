create database marge;
use marge;
create table student(name varchar(20) , email varchar(20) , roll int);
insert into student(name,email,roll) values ('aashish','aashish@mail.com',1),('jayu','jayu@mail.com',2);
select * from student;

create table result(roll int ,score int);
insert into result(roll,score) values (1,77),(2,44);

SELECT s.name, s.email, r.score, s.roll 
FROM student AS s 
JOIN result AS r ON s.roll = r.roll 
WHERE s.roll = 1;
