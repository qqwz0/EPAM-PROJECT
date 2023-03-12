import mysql.connector

# connect to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="qqwz0",
  password="12345"
)

# create a new database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE myfinalestdatabase")

# connect to the MySQL server and select the database
mydb = mysql.connector.connect(
  host="localhost",
  user="qqwz0",
  password="12345",
  database="myfinalestdatabase"
)

# create the department table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE department (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# create the employee table
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, department_id INT, name VARCHAR(255), dob DATE, salary DECIMAL(10, 2))")

# insert test data into the department table
mycursor.execute("INSERT INTO department (name) VALUES ('Sales')")
mycursor.execute("INSERT INTO department (name) VALUES ('Marketing')")

# insert test data into the employee table
mycursor.execute("INSERT INTO employee (department_id, name, dob, salary) VALUES (1, 'Maxym Zalizko', '1999-01-01', 50000)")
mycursor.execute("INSERT INTO employee (department_id, name, dob, salary) VALUES (1, 'Jane Doe', '1777-01-01', 60000)")
mycursor.execute("INSERT INTO employee (department_id, name, dob, salary) VALUES (2, 'John Doe', '1888-01-01', 70000)")
mycursor.execute("INSERT INTO employee (department_id, name, dob, salary) VALUES (2, 'Kyadae Tenz', '2000-01-01', 80000)")

# commit the changes
mydb.commit()