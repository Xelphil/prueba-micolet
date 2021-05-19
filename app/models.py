import os
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, VARCHAR
from app import db

class Micotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mujer = Column(VARCHAR(2), nullable=True)
    hombre = Column(VARCHAR(2), nullable=True)
    infantil = Column(VARCHAR(2), nullable=True)

    def __repr__(self):
        return '<Micotel {}>'.format(self.email)
