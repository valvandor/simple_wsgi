"""
Module is responsible for communication between WSGI-server and python application
"""
from typing import List
from wsgiref import simple_server


class WSGIFramework:
    """
    Base class of WSGI-framework
    """
    def __init__(self, config: dict):
        self._config = config

    @property
    def _port(self) -> int:
        assert 'port' in self._config
        return self._config['port']

    @property
    def _root_path(self) -> str:
        assert 'root_path' in self._config
        return self._config['root_path']

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

    def run(self):
        """
        Entry point for running WSGI-application
        """

        print(f"Serving {self._root_path} on port {self._port}, ctrl+c to stop")
        httpd = simple_server.make_server("", self._port, self)

        print('Check for a link: {}'.format(f"http://localhost:{self._port}/wsgi/1.cgi.app.py"))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down.")
            httpd.server_close()
