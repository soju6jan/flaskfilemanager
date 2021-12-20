# -*- coding: utf-8 -*-
"""
Rich File Manager for Flask
"""
from .filemanager import filemanager_blueprint as blueprint
from .filemanager import init, set_access_control_function


__author__ = 'Stephen Brown (Little Fish Solutions LTD)'


def plugin_load():
    from framework import app, path_app_root
    #app.config['FLASKFILEMANAGER_FILE_PATH'] = path_app_root
    app.config['FLASKFILEMANAGER_FILE_PATH'] = '/'
    init(app)

def plugin_unload():
    pass


plugin_info = {
    'version' : '1.0.0',
    'name' : '파일 매니저',
    'category_name' : 'system',
    'icon' : '',
    'developer' : 'soju6jan',
    'description' : 'RichFilemanager를 Flask에서 동작하도록 한 FlaskFileManager 포크',
    'home' : 'https://github.com/soju6jan/flaskfilemanager',
    'more' : '',
}

import os
from tool_base import ToolUtil
ToolUtil.save_dict(plugin_info, os.path.join(os.path.dirname(__file__), 'info.json'))
