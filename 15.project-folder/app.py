from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)

# Configure connection
conn_str = (
     "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ARUTPERUNJOTHI;"
    "DATABASE=MyFlaskDB;"
    "Trusted_Connection=yes;"
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']

    cursor.execute("INSERT INTO Users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()

    return redirect('/users')


@app.route('/users')
def users():
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    return render_template('users.html', users=data)


if __name__ == '__main__':
    app.run(debug=True)
