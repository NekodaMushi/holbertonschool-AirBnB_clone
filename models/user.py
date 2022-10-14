#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Public Class: basics informations on User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
