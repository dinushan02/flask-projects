from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    fruits = ["Apple", "Banana", "Cherry"]
    return render_template('home.html', fruits=fruits)

app.run()
