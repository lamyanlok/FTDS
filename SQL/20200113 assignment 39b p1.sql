CREATE TABLE employee (
  employee_id INTEGER,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  salary INTEGER,
  contract_length INTEGER,
  PRIMARY KEY (employee_id)   
);

INSERT INTO employee(employee_id,first_name, last_name, salary, contract_length) VALUES(1,'Steven', 'King', 10000, 3);
INSERT INTO employee(employee_id,first_name, last_name, salary, contract_length) VALUES(2,'Neena', 'Kochhar', 8000, 2);
INSERT INTO employee(employee_id,first_name, last_name, salary, contract_length) VALUES(3,'David', 'Austin', 12000, 2);
INSERT INTO employee(employee_id,first_name, last_name, salary, contract_length) VALUES(4,'Nancy', 'Greenberg', 3000, 1);

select * from employee;
select first_name, last_name from employee where salary > 5000 and salary < 11000;
select * from employee where contract_length < 2;
INSERT INTO employee(employee_id,first_name, last_name, salary, contract_length) VALUES(5,'Brian', 'Brian', 12000, 2);
INSERT INTO employee(employee_id,first_name, last_name, salary, contract_length) VALUES(6,'Darren', 'Darren', 30000, 3);
update employee set salary  = 8000, contract_length = 2 where first_name ='Nancy';
