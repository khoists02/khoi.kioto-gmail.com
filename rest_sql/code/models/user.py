from db import db
from sqlalchemy import Column, String, Integer
from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            'username': self.username,
        }

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, name):
        return cls.query.filter_by(username=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
