from django.shortcuts import render
from register.forms import UserForm

# Create your views here.
def register_view(request):
    user_form = UserForm(request.POST or None)
    if user_form.is_valid():
        user_form.save()
        user_form = UserForm()
    template_name="register.html"
    context = dict(registerForm=user_form)
    return render(request,template_name,context)