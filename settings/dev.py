from base import *

DEBUG = False

INSTALLED_APPS.append('debug_toolbar')

DISQUS_API_KEY = 'ZruTajAt8E3Ao1F2fzL2Dx9VUra9u0XABGKdSLXtAIHN3gL0qoUwJYywaqMEKkB8'
DISQUS_WEBSITE_SHORTNAME = 'codeinstitutesocialstaging'

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_nbWefqblVg8HnYsFmpcld8qj')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_N35jP51CRqW4FKBMa8MAL1A4')

# Paypal environment variables
SITE_URL = 'http://wearesocial2016.herokuapp.com'
PAYPAL_NOTIFY_URL = 'http://wearesocial2016.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'aaron@codeinstitute.net'
