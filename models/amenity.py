#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = 'amenities'
    if models.storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place',
            secondary='place_amenity',
            viewonly=False
            )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)