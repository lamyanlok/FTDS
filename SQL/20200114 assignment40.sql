DROP DATABASE IF EXISTS assignment40A;
CREATE DATABASE assignment40A;
use assignment40A;

CREATE TABLE Departments (
  Code INTEGER,
  Name TEXT,
  Budget REAL,
  PRIMARY KEY (Code)   
);

CREATE TABLE Employees (
  SSN INTEGER,
  Name TEXT ,
  LastName TEXT ,
  Department INTEGER,
  PRIMARY KEY (SSN), 
  FOREIGN KEY (Department) REFERENCES Departments(Code)
); 

INSERT INTO Departments (Code, Name, Budget) VALUES(14,'IT',65000);
INSERT INTO Departments (Code, Name, Budget) VALUES(37,'Accounting',15000);
INSERT INTO Departments (Code, Name, Budget) VALUES(59,'Human Resources',240000);
INSERT INTO Departments (Code, Name, Budget) VALUES(77,'Research',55000);

INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(123234877,'Michael', 'Rogers',14);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(152934485,'Anand', 'Manikutty',14);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(222364883,'Carol', 'Smith',37);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(326587417,'Joe', 'Stevens',37);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(332154719,'Mary-Anne', 'FOSTER',14);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(332569843,'George', 'ODonnell',77);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(546523478,'John', 'Doe',59);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(631231482,'David', 'Smith',77);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(654873219,'Zacary', 'Efron',59);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(745685214,'Eric', 'Goldsmith',59);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(845657245,'Elizabeth', 'Doe',14);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(845657246,'Kumar', 'Swamy',14);

select * from Employees where Department = 37 or Department = 77;
select * from Employees where LastName LIKE 'S%';
select sum(Budget) from Departments;
select count(SSN), Department from Employees group by Department;
select * from Employees join Departments on Departments.Code = Employees.Department;
select Employees.name, LastName from Employees join Departments on Departments.Code = Employees.Department where Budget > 60000;
select Name from Departments where Budget > (select avg(budget) from Departments);
select count(SSN), Department, Departments.Name from Employees join Departments on Departments.Code = Employees.Department group by Department having count(SSN) > 2;
select code from departments where budget = (select min(Budget) from Departments where Budget > (select min(budget) from Departments));
select name, LastName from employees where department = (select code from departments where budget = (select min(Budget) from Departments where Budget > (select min(budget) from Departments)));
INSERT INTO Departments (Code, Name, Budget) VALUES(11,'Quality Assurance',40000);
INSERT INTO Employees (SSN, Name, LastName, Department) VALUES(847219811,'Mary', 'Moore',11);
DELETE from Employees where department in (select distinct code from departments where budget >= 60000);
