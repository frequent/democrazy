# ==============================================================================
# init_app urls
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------

from django.conf.urls import url
from mysite.init_app import views

urlpatterns = [
  #url(r'^(?P<filename>(robots.txt)|(humans.txt))$', views.crawler, name='crawler'),

  # home/i18n
  url(r"^$", views.index, name="index"),
]