# ==============================================================================
# init_app views
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------

from django.shortcuts import render

#def index(request):
#    return HttpResponse("Hello, world.<a href='/admin'>Link</a>")

# ------------------------------ Landing Page ----------------------------------
def index(request):
  return render(request,'init_app/index.html', context=dict())

# ---------------------------- About Page -----------------------------------
def about(request):
  return render(request, 'static/about.html', context=dict())

# ---------------------------- Data Protection Page ----------------------------------
def confidentiality(request):
  return render(request, 'static/confidentiality.html', context=dict())

# ---------------------------- Documentation Page ----------------------------------
def documentation(request):
  return render(request, 'static/documentation.html', context=dict())

# ---------------------------- Language Page -------------------------------
def account_language(request):
  return render(request, 'static/language.html', context=dict())