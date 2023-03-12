from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="qqwz0",
    password="12345",
    database="myfinalestdatabase"
)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db.cursor()
        sql = "INSERT INTO my_table (name) VALUES (%s)"
        val = (name,)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM my_table WHERE id = %s", (id,))
    data = cursor.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        sql = "UPDATE my_table SET name = %s WHERE id = %s"
        val = (name, id)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    cursor.close()
    return render_template('edit.html', data=data)

@app.route('/delete/<int:id>')
def delete(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM my_table WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))