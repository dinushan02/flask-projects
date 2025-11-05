from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/verify', methods=['POST'])
def verify():
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template('verify.html', email=email, password=password)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would typically validate the user credentials
        email = request.form.get('email')
        password = request.form.get('password')
        return f"Logged in with {email}"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
