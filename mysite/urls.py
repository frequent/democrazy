# ==============================================================================
# Voty GLOBAL Url Configuration
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------
# The "urlpatterns" list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [

    # required for multi-language
    url(r"^i18n/", include("django.conf.urls.i18n")),

]

urlpatterns += i18n_patterns(
    url(r"", include("mysite.init_admin.urls")),
    url(r"^language$", TemplateView.as_view(template_name="language.html")),
    url(r"", include("mysite.init_app.urls")),
)  + static(
  settings.STATIC_URL, document_root=settings.STATIC_ROOT
)