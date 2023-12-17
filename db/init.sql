CREATE DATABASE company;
USE company;

CREATE TABLE employees (
  full_name VARCHAR(50),
  job_title VARCHAR(50)
);

INSERT INTO employees 
  (full_name, job_title)
VALUES
  ('Jennifer Wallace', 'Manager'),
  ('John Smith', 'Engineer');
