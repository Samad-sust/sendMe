from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
print('Working fine init')
# if os.environ['myproject'] == 'prod':
myproject = 'dev'
if myproject == 'prod':
   from .prod import *
else:
   from .dev import *