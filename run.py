import os
from framework.main import WSGIFramework


if __name__ == "__main__":
    # create an object for the WSGI application based on config
    config = {
        'root_path': os.getcwd(),
        'port': 8000
    }
    application = WSGIFramework(config)
    application.run()
