# ==============================================================================
# init_admin urls
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------

from django.conf.urls import url
from django.contrib import admin

from mysite.init_admin import views

urlpatterns = [
  
  # superusers
  url(r"^admin/", admin.site.urls),

  url(r"^register/", views.register_request, name="register"),
  url(r"^login/", views.login_request, name="login"),
  url(r"^logout/", views.logout_request, name= "logout"),
  url(r"^activate/(?P<uidb64>.*)/(?P<token>.*)/", views.activate, name= "activate"),
]