#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class, contains 'name' and relationship to City """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    
    def cities(self):
        """ Getter for cities """
        if models.storage_t == 'db':
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
        else:
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
