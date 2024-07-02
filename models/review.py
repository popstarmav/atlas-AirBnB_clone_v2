#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    tablename = Column 
    place_id = ""
    user_id = ""
    text = ""
