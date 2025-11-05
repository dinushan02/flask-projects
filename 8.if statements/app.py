from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    is_logged_in = True
    return render_template('home.html', logged_in=is_logged_in)

app.run()
