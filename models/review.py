#!/usr/bin/python3
"""Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User's Review"""
    place_id = ""
    user_id = ""
    text = ""
