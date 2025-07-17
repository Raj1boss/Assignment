# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 16:41:12 2025

@author: rakumar
"""

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret'
    JWT_SECRET_KEY = 'jwt-secret-key'