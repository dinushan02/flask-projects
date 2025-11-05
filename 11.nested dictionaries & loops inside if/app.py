from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    user_profile = {
        "name": "Hi Bro",
        "projects": [
            {"title": "Flask Website", "status": "Completed"},
            {"title": "AI Chatbot", "status": "In Progress"},
            {"title": "Data Dashboard", "status": "Planned"}
        ]
    }
    show_projects = True
    return render_template('home.html', user=user_profile, show=show_projects)

@app.route('/about')
def about():
    return render_template('about.html')


app.run()
