"""Module for managing application"""

import os
from utils import create_app

app = create_app(os.getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    app.run()
