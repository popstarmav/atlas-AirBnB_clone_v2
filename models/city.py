#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    from models import storage_type
    __tablename__ = 'cities'
    
    if models.storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', back_populates='city', cascade='all, delete')
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initialization of city"""
        super().__init__(*args, **kwargs)