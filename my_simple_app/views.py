"""
Module containing WSGI-application controllers — views
"""
from framework.templator import render


class Index:
    """
    Handler for main page – '/'
    """
    def __call__(self):
        return '200 - OK', render('index.html')
