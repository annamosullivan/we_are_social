from base import *

HOME_DIR = os.path.expanduser('~')

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DISQUS_API_KEY = 'ZruTajAt8E3Ao1F2fzL2Dx9VUra9u0XABGKdSLXtAIHN3gL0qoUwJYywaqMEKkB8'
DISQUS_WEBSITE_SHORTNAME = 'codeinstitutesocialstaging'

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_nbWefqblVg8HnYsFmpcld8qj')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_N35jP51CRqW4FKBMa8MAL1A4')

# Paypal environment variables
SITE_URL = 'https://wearesocial2016.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://wearesocial2016.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'annamarieosullivan76@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(HOME_DIR, 'we_are_social', 'emails')
