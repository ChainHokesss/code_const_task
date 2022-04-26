from enum import unique
import sqlalchemy as db
from sqlalchemy.orm import declarative_base, relationship
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(50))
    # product = relationship('Product', cascade="all,delete", backref="user")


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(password)


class Product(Base):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    price = db.Column(db.Integer)
    number = db.Column(db.Integer)

    # user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
