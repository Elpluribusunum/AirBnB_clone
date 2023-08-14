#!/usr/bin/python3
"""the magic method __init__ for the models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
