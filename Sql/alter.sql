use class;
CREATE TABLE student(roll int,name VARCHAR(50),dept VARCHAR(50));
insert into student values (1,'aashu','it');
SELECT * from student;
alter table student add score int; 

select name , dept , score, grad, pass from student join class on student.roll = class.roll;

select max(score), name from student  GROUP BY name;

select count(pass),name from student GROUP BY name HAVING score > 100;