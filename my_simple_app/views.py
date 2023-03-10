"""
Module containing WSGI-application controllers — views
"""
from framework.templator import render


class Index:
    """
    Handler for main page – '/'
    """
    def __call__(self, request):
        return '200 - OK', render('index.html')


class Another:
    """
    Handler for main page – '/another'
    """
    def __call__(self, request):
        return '200 - OK', render('another.html')
