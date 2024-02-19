#!/usr/bin/python3
"""This module instantiates an storage session"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ


if environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
