"""
Module contain logic for request creation
"""
from quopri import decodestring as quopri_decodestring
from framework import utils


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
                post_data = self._get_wsgi_input_data(environ)
                print(f'POST-data: {post_data}')
                request['data'] = post_data

        return request

    @staticmethod
    def _get_parsed_params(data: str) -> dict:
        """
        Parse data containing request params into a dict

        Side effects:
            - normalization of data values

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
                normalized_value = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
                params[k] = quopri_decodestring(normalized_value).decode('UTF-8')
        return params

    def _get_wsgi_input_data(self, environ: dict) -> dict:
        """
        Gets data from raw content of body

        Returns:
            parsed params as a data
        """
        data = utils.get_decoded_data(size=int(environ['CONTENT_LENGTH']), io_object=environ['wsgi.input'])
        return self._get_parsed_params(data)
