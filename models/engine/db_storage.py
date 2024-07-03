#!/usr/bin/python3
import os
import sys
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
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        objects = {}
        try:
            if cls:
                if isinstance(cls, str):
                    cls = getattr(sys.modules[__name__], cls)  # Get class dynamically by name
                    objects = {obj.id: obj for obj in self.__session.query(cls).all()}
            else:
                for class_ in classes.values():
                    objects.update({obj.id: obj for obj in self.__session.query(class_).all()})
        except SQLAlchemyError as e:
            print(f"Error querying {cls.__name__ if cls else 'all classes'}: {str(e)}")
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
        print(" Tables should be created. ")
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

