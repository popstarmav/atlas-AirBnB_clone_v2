#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    from models import storage_type
    
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan', passive_deletes=True)
    else:
        name = ""
        cites = ""

    @property
    def cities(self):
        from models.city import City
        city_list = City.name
        for city in list(self.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
