# ==============================================================================
# keep track of tests, since they can't be commmitted
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
  activate('en')

  url = reverse('about', args=[])
  self.assertEqual(url, '/en/about')

  resolver = resolve('/en/about')
  self.assertEqual(resolver.view_name, 'about')

  '''
  routes = {
    "/about": init_app_views.about,
    "/confidentiality": init_app_views.confidentiality,
    "/documentation": init_app_views.documentation,
    "/language": init_app_views.account_language
  }

  for route,function in routes.items():
    found = resolve(route)
    self.assertEqual(found.func, function)
  '''

