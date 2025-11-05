from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    user_info = {
        "name": "Hi Bro",
        "age": 25,
        "country": "Sri Lanka"
    }
    return render_template('home.html', user=user_info)

app.run()
