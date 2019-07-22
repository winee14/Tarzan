from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Winnie14$',
    database='tarzan'
)

mycursor = mydb.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        sql = "INSERT INTO MyUsers (firstname, lastname) VALUES (%s, %s)"
        val = (firstName, lastName)
        mycursor.execute(sql, val)
        mydb.commit()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
