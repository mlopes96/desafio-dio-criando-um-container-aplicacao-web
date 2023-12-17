from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def write_employee(employee_name: str, title_job: str):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'company'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "INSERT INTO employees (full_name, job_title) VALUES (%s, %s)"
    values = (employee_name, title_job)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def employee_data():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'company'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT full_name, job_title FROM employees')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index():
    #write_employee("Json Script","Analyst")
    return jsonify({'Employee Data': employee_data()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
