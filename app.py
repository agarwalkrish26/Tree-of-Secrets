from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for sessions

# Load configuration
def load_config():
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"users": {}, "messages": {}}
    except json.JSONDecodeError:
        return {"users": {}, "messages": {}}

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    config = load_config()
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in config['users'] and config['users'][username] == password:
        session['username'] = username
        return redirect(url_for('main'))
    
    flash('Invalid username or password')
    return redirect(url_for('login'))

@app.route('/main')
@login_required
def main():
    return render_template('main.html')

@app.route('/message')
@login_required
def message():
    config = load_config()
    username = session['username']
    secret_message = config['messages'].get(username, "No message found")
    return render_template('message.html', message=secret_message)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 