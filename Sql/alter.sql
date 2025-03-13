use class;
CREATE TABLE student(roll int,name VARCHAR(50),dept VARCHAR(50));
insert into student values (1,'aashu','it');
SELECT * from student;
alter table student add score int; 

select name , dept , score, grad, pass from student join class on student.roll = class.roll;