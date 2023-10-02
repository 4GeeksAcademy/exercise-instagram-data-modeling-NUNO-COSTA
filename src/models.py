import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    bio = Column(String(300))
    profile_image_url = Column(String(255))
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    caption = Column(String(250))
    image_url = Column(String(255), nullable=False)
    created_at = Column(String(50))

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')
    

    comments = relationship('Comment', back_populates='post')
    likes = relationship('Like', back_populates='post')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    created_at = Column(String(250))


    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User')


    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship('Post', back_populates='comments')

class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True)


    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User')


    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship('Post', back_populates='likes')



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
