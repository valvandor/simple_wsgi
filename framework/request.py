"""
Module contain logic for request creation
"""


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
