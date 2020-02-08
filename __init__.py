"""
Rich File Manager for Flask
"""

from .filemanager import filemanager_blueprint as blueprint
from .filemanager import init, set_access_control_function

__author__ = 'Stephen Brown (Little Fish Solutions LTD)'

def plugin_load():
    from framework import app
    app.config['FLASKFILEMANAGER_FILE_PATH'] = r'/'
    init(app)

def plugin_unload():
    pass


