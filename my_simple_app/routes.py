"""
Module with WSGI-application routes
"""
from .views import Index

urls = {
    '/': Index(),
}
