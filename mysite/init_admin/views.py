# ==============================================================================
# init_admin views
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from mysite.init_admin.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _

# ---------------------------- Register User ---------------------------------------
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, _("Registration successful."))
			return redirect("/")
		messages.error(request, _("Unsuccessful registration. Invalid information."))
	form = NewUserForm
	return render (request=request, template_name="init_admin/register.html", context={"register_form": form})


# ---------------------------- Login User ---------------------------------------
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, _("Logged in successfully"))
				return redirect("/")
			else:
				messages.error(request, _("Invalid email or password."))
		else:
			messages.error(request, _("Invalid email or password."))
	form = AuthenticationForm()
	return render(request=request, template_name="init_admin/login.html", context={
    "login_form":form
  })

# ---------------------------- Logout User ---------------------------------------
def logout_request(request):
	logout(request)
	messages.info(request, _("Logged out successfully.")) 
	return redirect("/")