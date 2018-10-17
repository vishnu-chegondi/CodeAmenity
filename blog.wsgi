import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/")

from Blog.blog import app as application
application.secret_key = 'thisismyblog3'
