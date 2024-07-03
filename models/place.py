#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
import models
metadata = Base.metadata

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False),
                      )
class Place(BaseModel, Base):
    from models import storage_type
    __tablename__ = 'places'

    if storage_type == 'db':

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=True)
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Float, nullable=True)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
        reviews = relationship(
            'Review', cascade='all, delete', backref='place')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False,
            backref='place_amenities')

    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0.0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if storage_type != 'db':
        @property
        def reviews(self):
            """review getter"""
            review_list = []
            reviews = list(models.storage.all(Review).values)
            for review in reviews:
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            """getter for amenities"""
            amenities_list = []
            amenities = list(models.storage.all(Amenity).values)
            for amenity in amenities:
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list
        
        @amenities.setter
        def amenities(self, obj):
            """add an amenity"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)