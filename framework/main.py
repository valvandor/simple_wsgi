"""
Module is responsible for communication between WSGI-server and python application
"""
from typing import List


class WSGIFramework:
    """
    Base class of WSGI-framework
    """

    def __call__(self, environ: dict, start_response) -> List[bytes]:
        """
        Args:
            environ: environment variable dictionary
            start_response: request handler

        Returns:
            list with byte string
        """
        status = "200 OK"  # HTTP Status
        headers = [("Content-type", "text/plain; charset=utf-8")]

        start_response(status, headers)
        body = 'Hello from wsgi-framework'
        return [body.encode('utf-8')]
