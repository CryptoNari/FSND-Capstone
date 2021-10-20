import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


'''
setup_db(app)
    setup flask application with SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Table: Test
Have name and ID
'''

class Test(db.Model):  
  __tablename__ = 'tests'

  id = Column(Integer(), primary_key=True)
  name = Column(String)

  def __init__(self, name):
    self.name = name

  def format(self):
    return {
      'id': self.id,
      'name': self.name
    }
