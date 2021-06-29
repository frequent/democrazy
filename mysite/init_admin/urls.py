# ==============================================================================
# init_admin urls
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
  
  # superusers
  url(r"^admin/", admin.site.urls),

]