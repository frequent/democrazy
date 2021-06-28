# ==============================================================================
# Voty GLOBAL Url Configuration
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------
# The "urlpatterns" list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/

#from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [

    # required for multi-language
    url(r"^i18n/", include("django.conf.urls.i18n")),

]

urlpatterns += i18n_patterns(
    url(r"", include("mysite.init_admin.urls")),
    #path('', views.index, name='index'),
    url(r"", include("mysite.init_app.urls")),
)