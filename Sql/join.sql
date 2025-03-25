create table t1(roll int ,name VARCHAR(25),subj VARCHAR(20));
insert into t1 VALUES (1,'aashu','Che'),(2,'veer','m1'),(3,'raaj','m2');

create table t2(roll int ,teacher VARCHAR(25));
insert into t2 VALUES (1,'aaryan'),(3,'sanket'),(50,'moru');
SELECT * from t1;
SELECT * from t2;

SELECT roll,name,teacher from t1 as t1
join t2 as t2 on t1.roll = t2.roll;


