from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
app_mode = os.environ.get('SEND_ME_DEVELOPMENT_MODE')
if app_mode == 'prod':
   from .prod import *
else:
   from .dev import *