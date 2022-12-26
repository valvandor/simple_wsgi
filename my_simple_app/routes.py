"""
Module with WSGI-application routes
"""
from .views import Index, Another

urls = {
    '/': Index(),
    '/another/': Another(),
}
