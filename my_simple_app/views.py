"""
Module containing WSGI-application controllers — views
"""


class Index:
    """
    Handler for main page – '/'
    """
    def __call__(self):
        return '200 - OK', 'OK (WSGI app is working)'
