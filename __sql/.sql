-- Create database
CREATE DATABASE department_management;

-- Switch to the newly created database
USE department_management;

-- Create department table
CREATE TABLE department (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

-- Create employee table
CREATE TABLE employee (
  id INT NOT NULL AUTO_INCREMENT,
  department_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  date_of_birth DATE NOT NULL,
  salary DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (department_id) REFERENCES department(id)
);

-- Insert test data into department table
INSERT INTO department (name)
VALUES ('Sales'), ('Marketing');

-- Insert test data into employee table
INSERT INTO employee (department_id, name, date_of_birth, salary)
VALUES
  (1, 'Maxym Zalizko', '1999-01-01', 50000),
  (1, 'Jane Doe', '2000-02-15', 55000),
  (2, 'Harbour Gekko', '1985-05-20', 60000);