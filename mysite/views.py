#from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse("Hello, world.<a href='/admin'>Link</a>")

# ------------------------------ Landing Page ----------------------------------
def index(request):
    return render(
        request,
        'init_app/index.html',
        context=dict()
    )