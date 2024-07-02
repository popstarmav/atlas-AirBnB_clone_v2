#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import models

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def save(self):
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy.pop('_sa_instance_state', None)
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
