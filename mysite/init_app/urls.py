# ==============================================================================
# Voty init_admin urls
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------

from django.conf.urls import url
from django.views import generic

from . import views

urlpatterns = [
  #url(r'^(?P<filename>(robots.txt)|(humans.txt))$', views.crawler, name='crawler'),

  # home/i18n
  url(r"^$", views.index, name="index"),
]