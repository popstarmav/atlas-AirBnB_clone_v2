#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Review(BaseModel, Base):
    from models import storage_type
    __tablename__ = 'Review'

    if  storage_type == 'db"':
        place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
        user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        storage_type = ""
        place_id = ""
        user_id = ""
        text = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

