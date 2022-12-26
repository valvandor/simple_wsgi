"""
Module with handlers for unsuccessful response
"""


class PageNotFound404:
    """
    Handler for non-existed page

    Returns:
        tuple with code and error message
    """
    def __call__(self):
        return '404 - NOT FOUND', 'Sorry, page not found'
