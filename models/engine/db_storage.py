#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        if cls:
            try:
                objects = {obj.id: obj for obj in self.__session.query(cls).all()}
            except SQLAlchemyError as e:
                print(f"Error querying {cls.__name__}: {str(e)}")
                objects = {}
        else:
            try:
                for clazz in classes:  # Add other classes here
                    for obj in self.__session.query(clazz).all():
                        objects[obj.id] = obj
            except SQLAlchemyError as e:
                print(f"Error querying all classes: {str(e)}")
                objects = {}
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

