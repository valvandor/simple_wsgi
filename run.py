import os
from wsgiref import simple_server
from framework.main import WSGIFramework


if __name__ == "__main__":
    # create an object for the WSGI application
    application = WSGIFramework()

    port = 8000
    root_path = os.getcwd()

    httpd = simple_server.make_server("", port, application)
    print(f"Serving {root_path} on port {port}, ctrl+c to stop")
    print('Check for a link: {}'.format(f"http://localhost:{port}/wsgi/1.cgi.app.py"))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
        httpd.server_close()
