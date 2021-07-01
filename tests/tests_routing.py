# ==============================================================================
# keep track of tests - navigation/routing
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------
# setup
from django.utils.translation import activate
from django.urls import resolve, reverse, translate_url, LocalePrefixPattern

from mysite.init_app import views as init_app_views

def test_url_route_validation(self):
  ''' validate all routes work '''

  # testing in en-us
  lang = 'en'
  slash = '/'
  activate(lang)

  routes = {
    "about": init_app_views.about,
    "confidentiality": init_app_views.confidentiality,
    "documentation": init_app_views.documentation,
    "language": init_app_views.language
  }

  for route,function in routes.items():
    route_i18n = slash + lang + slash + route 
    url = reverse(route, args=[])
    self.assertEqual(url, route_i18n)  

    resolver = resolve(route_i18n)
    self.assertEqual(resolver.view_name, route)