from flask import render_template, request, Flask, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form=LoginForm()
    if form.validate_on_submit():
        print("datos enviados correctamente")
        return redirect(url_for('micotel'))
    else:
        print("no")
    return render_template('index.html', form=form)

@app.route('/micotel', methods=['GET', 'POST'])
def micotel():
    return render_template('micotel.html')