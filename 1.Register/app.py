"""from flask import Flask,render_template,request
# Initialize flask app development
app=Flask(__name__)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('Register.html')

@app.route("/confirm",methods=['POST','GET'])
def register():
    if request.method=='POST':
        n = request.form.get('name')
        a = request.form.get('age')
        c = request.form.get('city')
        return render_template('confirm.html',name=n,age=a,city=c)


if __name__== "__main__":
    app.run(debug=True)"""

# Import necessary functions and classes from Flask
from flask import Flask, render_template, request

# Create a Flask web application instance
app = Flask(__name__)

# Route for homepage (two routes: '/' and '/register' both go to the same function)
@app.route('/')
@app.route('/register')
def homepage():
    # Render the Register.html page when user visits the homepage or /register
    return render_template('Register.html')

# Route for handling the form submission
@app.route("/confirm", methods=['POST', 'GET'])
def register():
    # Check if the request method is POST (i.e., form was submitted)
    if request.method == 'POST':
        # Get form values using 'request.form.get'
        n = request.form.get('name')  # Get the 'name' field value
        a = request.form.get('age')   # Get the 'age' field value
        c = request.form.get('city')  # Get the 'city' field value

        # Pass the retrieved values to the 'confirm.html' template
        return render_template('confirm.html', name=n, age=a, city=c)

# This block ensures the app runs only when this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask server in debug mode
