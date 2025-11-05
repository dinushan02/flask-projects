from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    username = "Hi Bro"   # your data
    return render_template('home.html', name=username)

app.run()
