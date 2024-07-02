#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan', passive_deletes=True)

    @property
    def cities(self):
        city_list = City.name
        for city in list(self.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
