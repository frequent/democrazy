# ==============================================================================
# init_admin models
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------
from django.contrib.auth.models import User
from django.conf import settings

# thx https://stackoverflow.com/a/64075027
User._meta.get_field('email')._unique = True