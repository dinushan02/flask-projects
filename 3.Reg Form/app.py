from flask import Flask, render_template, request, redirect, url_for
import urllib.parse

app = Flask(__name__)

# Jinja filter for urlencode (used for Unsplash image query)
@app.template_filter('urlencode')
def urlencode_filter(s):
    return urllib.parse.quote_plus(s)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Here you could add validation or save to DB
        print(f"Registered user: {name}")

        return redirect(url_for('courses'))
    return render_template('register.html')

@app.route('/courses')
def courses():
    course_list = [
        {"name": "Python Basics", "level": "Beginner"},
        {"name": "Advanced JavaScript", "level": "Intermediate"},
        {"name": "Machine Learning", "level": "Advanced"},
        {"name": "React & Flask Integration", "level": "Intermediate"},
        {"name": "Data Analysis with Pandas", "level": "Intermediate"},
        {"name": "HTML & CSS Mastery", "level": "Beginner"},
    ]
    return render_template('courses.html', courses=course_list)

if __name__ == "__main__":
    app.run(debug=True)
