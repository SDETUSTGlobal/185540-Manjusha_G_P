from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'my_first_db'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        First_Name = details['fname']
        Last_Name = details['lname']
        Employee_ID = details['emp_id']
        Company_Name = details['com_name']
        Email_ID = details['mail']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login_details(First_Name, Last_Name, Employee_ID, Company_Name, Email_ID) VALUES (%s, %s, %s, %s, %s )", (First_Name, Last_Name, Employee_ID, Company_Name, Email_ID))
        mysql.connection.commit()
        cur.close()
        return render_template('about.html', fn=details['fname'], ln=details['lname'], uid=details['emp_id'], cn=details['com_name'], eid=details['mail'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
