from db import db
from sqlalchemy import Column, String, Integer

class UserProfile(db.Model):
    __tablename__ = 'userprofile'

    id = Column(db.Integer, primary_key=True)
    address = Column(db.String)
    phone = Column(db.String(11))
    avatar = Column(db.String())
    user_id = Column(db.Integer)

    def __init__(self, address, phone, avatar, user_id):
        self.address = address
        self.phone = phone
        self.avatar = avatar
        self.user_id = user_id

    def json(self):
        return {'address': self.address, 'phone': self.phone, 'avatar': self.avatar, 'user_id': self.user_id}

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_to_database(cls, user_id):
        userprofile =  cls.query.filter_by(user_id=user_id).first()
        db.session.add(cls)
        db.session.commit()

    
    @classmethod
    def check_exists_user_id(cls, user_id):
      return cls.query.filter_by(user_id=user_id).first()