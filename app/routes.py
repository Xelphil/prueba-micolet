from flask import render_template, request, Flask, redirect, url_for
from app import app, db
from app.models import Micotel
from app.forms import LoginForm
import requests

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Micotel': Micotel}

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form=LoginForm()
    if form.validate_on_submit():
        response=requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=31f1d775cf294ae38d261fa83e65a103&email="+form.email.data)
        print(response.status_code)
        print(response.content)
        # if  == True:
        email=form.email.data
        # else:
        #     return redirect(url_for('index'))
        if form.mujer.data: 
            mujer = "Si"
        else: 
            mujer = "No"
        if form.hombre.data: 
            hombre = "Si"
        else: 
            hombre = "No"
        if form.infantil.data: 
            infantil = "Si"
        else: 
            infantil = "No"
        micotel = Micotel(email=email, mujer=mujer, hombre=hombre, infantil=infantil)
        try:
            db.session.add(micotel)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.add(micotel)
            db.session.commit()
        return redirect(url_for('micotel'))
    return render_template('index.html', form=form)

@app.route('/micotel', methods=['GET', 'POST'])
def micotel():
    return render_template('micotel.html')