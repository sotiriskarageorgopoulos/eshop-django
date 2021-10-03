from django.shortcuts import render
from register.models import UserModel
from django.db.models import Q

# Create your views here.
def setSessionVars(request,user):
    name = user[0].name
    surname = user[0].surname
    email = user[0].email
    street = user[0].street
    postal_code = user[0].postal_code
    city = user[0].city 
    province = user[0].province
    tel = user[0].tel

    request.session['name'] = name
    request.session['surname'] = surname
    request.session['email'] = email
    request.session['street'] = street
    request.session['postal_code'] = postal_code
    request.session['city'] = city
    request.session['province'] = province
    request.session['tel'] = tel

def login_view(request):
    template_name = "login.html"
    email = request.POST.get('email')
    password = request.POST.get('password')
    context = dict()
    if email is not None and password is not None:
        user = UserModel.objects.filter(Q(email=email) & Q(password=password))
        if user:
            setSessionVars(request,user)
            template_name = "main_page.html"
            context = dict()
            return render(request,template_name,context)
        else:
            error_text = "It is not a valid email or password"
            context = dict(error_text=error_text)
    
    return render(request,template_name,context)