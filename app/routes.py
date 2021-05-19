from flask import render_template, request, Flask, redirect, url_for
from app import app, db
from app.models import Micotel
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form=LoginForm()
    if form.validate_on_submit():
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
        micotel = Micotel(email=form.email.data, mujer=mujer, hombre=hombre, infantil=infantil)
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