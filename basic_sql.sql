create database cloudblitz01;
use cloudblitz01;
create table slaves( emp_id int primary key, first_name varchar(50) , last_name varchar(50) ,
 email varchar (50) , phone_no varchar (12), job_title varchar (50) , salary decimal(10,2),
department varchar(50));
 
 insert into slaves ( emp_id , first_name , last_name ,  email ,  phone_no , job_title , salary , department)
 values
(1, 'Dewansh' , 'Basotiya' , 'dewansh.basotiya01@gmail.com' , '9322162332' , 'Boss' , 70000 , 'it'),
(2, 'Krishna' , 'Dudhambe' , 'Krishna.basotiya01@gmail.com' , '8766678433' , 'ds' , 60000 , 'hr'),
(3, 'Vedant' , 'Mandle' , 'Vedant.basotiya01@gmail.com' , '8669403701' , 'da' , 50000 , 'it'),
(4, 'Prathmesh' , 'Nishane' , 'Prathmesh.basotiya01@gmail.com' , '8975589963' , 'cloud' , 40000 , 'non tech'),
(5, 'Arya' , 'Patil' , 'Arya.basotiya01@gmail.com' , '9881379205' , 'security' , 30000 , 'finance'),
(6, 'Sakshi', 'Kale', 'sakshi.kale01@gmail.com', '9812345678', 'analyst', 65000, 'finance'),
(7, 'Rohan', 'Sharma', 'rohan.sharma01@gmail.com', '9898989898', 'devops', 55000, 'it'),
(8, 'Sneha', 'Joshi', 'sneha.joshi01@gmail.com', '9765432109', 'hr executive', 48000, 'hr'),
(9, 'Amit', 'Yadav', 'amit.yadav01@gmail.com', '9123456780', 'support', 35000, 'non tech'),
(10, 'Pooja', 'Deshmukh', 'pooja.deshmukh01@gmail.com', '9345678123', 'accountant', 45000, 'finance');
     
select *from slaves;

alter table slaves drop column phone_no;
select *from slaves;

alter table slaves rename to employee;
select*from employee;

update employee set salary = 150000 where emp_id = 1;
select *from employee;

delete from employee where emp_id > 6;
select *from employee;
