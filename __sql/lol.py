import mysql.connector

# connect to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="qqwz0",
  password="12345"
)

# check if the database exists
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for db in mycursor:
  if 'myfinalestdatabase' in db:
    print("Database exists")
    break
else:
  print("Database does not exist")