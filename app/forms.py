from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    mujer = BooleanField('Moda Mujer')
    hombre = BooleanField('Moda Hombre')
    infantil = BooleanField('Moda Infantil')
    subcribirme = SubmitField('Subscribirme')
