"""
Module contain logic for request creation
"""
from io import BufferedReader


class RequestPreparer:
    """
    Class with helpful method for request preparation
    """

    def form_new_request(self, environ: dict) -> dict:
        """
        Creates new request

        Args:
            environ: a dictionary containing HTTP request variables

        Returns:
            request as a dict for WSGI-application
        """
        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'GET':
            params = self._get_parsed_params(data=environ['QUERY_STRING'])
            request['params'] = params
            print(f'GET-parameters: {params}')
        if method == 'POST':
            if environ.get('CONTENT_LENGTH'):
                data = self._get_wsgi_input_data(content_length=int(environ['CONTENT_LENGTH']),
                                                 input_data=environ['wsgi.input'])
                post_params = self._get_parsed_params(data)
            else:
                post_params = {}
            print(f'POST-data: {post_params}')
            request['data'] = post_params

        return request

    @staticmethod
    def _get_parsed_params(data: str) -> dict:
        """
        Parse data containing request params into a dict

        Args:
            data: data to parse

        Returns:
             request parameters as a dict
        """
        params = {}
        if data:
            items = data.split('&')
            for item in items:
                k, v = item.split('=')
                params[k] = v
        return params

    @staticmethod
    def _get_wsgi_input_data(content_length: int, input_data: BufferedReader) -> str:
        """
        Reads file-like object depending on the length of the content passed in the request

        Returns:
            decoded data
        """
        bytes_data = input_data.read(content_length)
        return bytes_data.decode(encoding='utf-8')
