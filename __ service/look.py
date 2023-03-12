# from flask import Flask, render_template
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'qqwz0'
# app.config['MYSQL_PASSWORD'] = '12345'
# app.config['MYSQL_DB'] = 'myfinalestdatabase'
#
# mysql = MySQL(app)
#
# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM employee")
#     data = cur.fetchall()
#     cur.close()
#     return render_template('employees_list.html', data=data)\

from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, template_folder='../__ templates', static_folder='../__ static')

@app.route('/')
def index():
    # Підключення до бази даних
    db = mysql.connector.connect(
        host="localhost",
        user="qqwz0",
        password="12345",
        database="myfinalestdatabase"
    )

    # Отримання даних з таблиці
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()

    # Передача даних у шаблон та відображення сторінки
    return render_template('employees_list.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)