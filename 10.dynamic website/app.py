from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    user_info = {
        "name": "Hi Bro",
        "age": 25,
        "country": "Sri Lanka",
        "skills": ["Python", "Flask", "HTML"]
    }
    is_logged_in = True
    return render_template('home.html', user=user_info, logged_in=is_logged_in)

@app.route('/about')
def about():
    return render_template('about.html')

app.run()
