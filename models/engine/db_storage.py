#!/usr/bin/python3
"""This module contains the class DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import environ
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Spins up a MySQL server for storing data for the application"""
    __engine = None
    __session = None

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):
        """Creates an initializes a MySQL database"""
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = environ.get('HBNB_MYSQL_DB')

        connection_string = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pwd, host, db)
        self.__engine = create_engine(connection_string, pool_pre_ping=True)
        Base.metadata.bind = self.__engine
        # if the environment is set to test
        # drop all the tables
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Query on the current db session"""
        obj_dict = {}
        if cls is not None:
            cls_name = DBStorage.classes[cls]
            query_result = self.__session.query(cls_name).all()
        else:
            query_result = []
            for class_ in DBStorage.classes.values():
                query_result.extend(self.__session.query(class_).all())
        
        for obj in query_result:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Adds an object to the current db session"""
        if obj is None:
            return
        self.__session.add(obj)
        
    def save(self):
        """Commits all changes to the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session"""
        if obj is not None:
            cls = DBStorage.classes[obj.__class__.__name__]
            self.__session.query(cls).filter(cls.id == obj.id).delete(synchronize_session='fetch')

    def reload(self):
        """Creates all tables in the db"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session()
