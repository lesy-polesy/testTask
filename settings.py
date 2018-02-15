import os.path

project_root = os.path.dirname(os.path.abspath(__file__))
mydb_name = ('%s/test.db' % project_root)
myviews_path = ('%s/views' % project_root)
myhost = 'localhost'
myport = 8080

try:
    from local_settings.py import *
except ImportError:
    pass