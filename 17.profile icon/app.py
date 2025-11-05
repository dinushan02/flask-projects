from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # For session handling

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        image_url = request.form['image_url']
        session['username'] = username
        session['image_url'] = image_url
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['username'], image_url=session['image_url'])

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'], image_url=session['image_url'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
