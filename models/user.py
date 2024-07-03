#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    from models import storage_type
    __tablename__ = 'users'

    
    if models.storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', backref='user', cascade='all, delete, delete-orphan')
        reviews = relationship("Review", backref="user", cascade="all, delete, delete-orphan")
    else:

        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initialization of user"""
        super().__init__(*args, **kwargs)