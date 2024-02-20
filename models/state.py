#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all,delete-orphan")

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns the list of City instances with
            state_id equals to the current State.id"""
            from models import storage
            cities_list = []
            all_models = storage.all()
            for key in all_models:
                key_class_name = all_models[key].__class__.__name__
                if key_class_name == 'City':
                    if all_models[key].state_id == self.id:
                        cities_list.append(all_models[key])
            return cities_list
