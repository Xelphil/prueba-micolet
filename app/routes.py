from flask import render_template, request, Flask
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/micolet', methods=['GET', 'POST'])
def micolet():
    email = request.form['email']
    preferencias = request.form['preferencias']
    print(email)
    return render_template('index.html', title='Home', user=user)