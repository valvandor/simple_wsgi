import os
from framework.main import WSGIFramework
from my_simple_app.routes import urls


if __name__ == "__main__":
    # create an object for the WSGI application based on config
    config = {
        'root_path': os.getcwd(),
        'port': 8000
    }
    application = WSGIFramework(config, routes=urls)
    application.run()
