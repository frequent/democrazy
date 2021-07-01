# ==============================================================================
# init_admin views
# ==============================================================================
#
# parameters (*default)
# ------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from mysite.init_admin.forms import NewUserForm
from mysite.init_admin.tokens import account_activation_token
from django.core.mail import EmailMessage

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import ugettext as _
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

# ---------------------------- Activate Account --------------------------------
def activate(request, uidb64, token):
  try:
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(id=uid)
  except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None

  if user is not None and account_activation_token.check_token(user, token):
    user.is_active = True
    user.save()
    messages.success(request, _("Thank you for your email confirmation. Now you can login your account."))
  else:
    messages.error(request, _("Activation link is invalid"))
  return redirect("/")

# ---------------------------- Register User ----------------------------------
def register_request(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_active = False
      user.save()

      current_site = get_current_site(request)
      mail_subject = _('Activate your account.')
      message = render_to_string('messages/account_activation_mail.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': account_activation_token.make_token(user),
      })
      to_email = form.cleaned_data.get('email')
      email = EmailMessage(
        mail_subject, message, to=[to_email]
      )
      email.send()
      messages.success(request, _("Please confirm your email address to complete the registration"))
      return redirect("/")

    messages.error(request, form.errors)
    # properly handle this with translateable strings _("Unsuccessful registration. Invalid information.")
  form = NewUserForm
  return render (request=request, template_name="init_admin/register.html", context={"register_form": form})

# ---------------------------- Login User ---------------------------------------
def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, _("Logged in successfully"))
        return redirect("/")
      else:
        messages.error(request, _("Invalid username or password."))
    else:
      messages.error(request, _("Invalid username or password."))
  form = AuthenticationForm()
  return render(request=request, template_name="init_admin/login.html", context={
    "login_form":form
  })

# ---------------------------- Logout User ---------------------------------------
def logout_request(request):
  logout(request)
  messages.info(request, _("Logged out successfully.")) 
  return redirect("/")