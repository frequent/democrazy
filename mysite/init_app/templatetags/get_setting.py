# -*- coding: utf-8 -*-
# ==============================================================================
# Make settings from .ini file accessible in templates
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/
# https://docs.djangoproject.com/en/dev/topics/settings/#custom-default-settings


from django.conf import settings
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# call: {% load get_setting %} then call {{ [setting_name]|get_setting %}
# note, this works only on first level settings
@register.filter(name='get_setting')
@stringfilter
def get_setting(my_setting):
  try:
    lookup_path = [x.upper() for x in my_setting.split(".")]
    if len(lookup_path) > 1:
      reply = settings.CUSTOM_DICT
      for key in lookup_path:
        #reply = getattr(reply, key.replace("-", "_"))
        # not sure this works
        reply = reply.get("settings", key.replace("-", "_"))
      return reply
    else:
      # no longer works
      #return getattr(settings, my_setting.upper())
      return settings.CUSTOM_DICT.get("settings", my_setting.upper())

  except AttributeError:
    print("y")
    return None