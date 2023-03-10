"""
Module is responsible for communication between WSGI-server and python application
"""
from typing import List, Callable
from wsgiref import simple_server

from framework.handlers import PageNotFound404
from framework.request import RequestPreparer


class WSGIFramework:
    """
    Base class of WSGI-framework
    """
    def __init__(self, config: dict, routes: dict):
        self._config = config
        self._routes = routes

    @property
    def _port(self) -> int:
        assert 'port' in self._config
        return self._config['port']

    @property
    def _root_path(self) -> str:
        assert 'root_path' in self._config
        return self._config['root_path']

    @property
    def request(self) -> RequestPreparer:
        return RequestPreparer()

    def __call__(self, environ: dict, start_response: Callable) -> List[bytes]:
        """
        Args:
            environ: environment variable dictionary
            start_response: request handler

        Returns:
            list with byte string
        """
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        # select view
        if path in self._routes:
            view = self._routes[path]
        else:
            view = PageNotFound404()

        request = self.request.form_new_request(environ)

        # run view
        status, body = view(request)
        headers = [("Content-type", "text/html")]

        start_response(status, headers)
        return [body.encode('utf-8')]

    def run(self):
        """
        Entry point for running WSGI-application
        """

        print(f"Serving {self._root_path} on port {self._port}, ctrl+c to stop")
        httpd = simple_server.make_server("", self._port, self)

        print('Check for a link: {}'.format(f"http://localhost:{self._port}/"))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down.")
            httpd.server_close()
