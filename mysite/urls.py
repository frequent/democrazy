# ==============================================================================
# GLOBAL Url Configuration
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------
# The "urlpatterns" list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from mysite.init_app import views

# required for multi-language
urlpatterns = [
    url(r"^i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    url(r"", include("mysite.init_admin.urls")),    
    url(r"^$", views.index, name="index"),

    # static pages
    url(r"^language$", views.language, name="language"),
    url(r"^about$", views.about, name="about"),
    url(r"^confidentiality$", views.confidentiality, name="confidentiality"),
    url(r"^documentation$", views.documentation, name="documentation"),

    url(r"", include("mysite.init_app.urls")),
)  + static(
  settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
