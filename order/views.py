from django.shortcuts import render
from order.models import (OrderModel,OrderedProductModel)
# Create your views here.
def getSessionVars(request):
    name = request.session['name']
    surname = request.session['surname'] 
    email = request.session['email']
    street = request.session['street']
    postal_code = request.session['postal_code']
    city = request.session['city']
    province = request.session['province']
    tel = request.session['tel']
    return dict(name=name,surname=surname,email=email,street=street,postal_code=postal_code,city=city,province=province,tel=tel)

def getFormData(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname') 
    email = request.POST.get('email')
    street = request.POST.get('street')
    postal_code = request.POST.get('postal_code')
    city = request.POST.get('city')
    province = request.POST.get('province')
    tel = request.POST.get('tel')
    clothes_code = request.POST.getlist('code')
    payment_method = request.POST.get('payment_method')
    ccn = request.POST.get('ccn')
    ccv = request.POST.get('ccv')
    total_cost = request.POST.get('total_cost')
    op_codes = dict()
    for c in clothes_code:
        op_codes[c] = int(request.POST.get(c))
    return dict(name=name,surname=surname,payment_method=payment_method,ccn=ccn,ccv=ccv,email=email,street=street,postal_code=postal_code,city=city,province=province,tel=tel,total_cost=total_cost,op_codes=op_codes)

def order_view(request):
    context = dict()
    template_name = "order.html"
    person = getSessionVars(request)
    form_data = getFormData(request)
    exists_personal_info = person["name"] and person["surname"] and person["email"] and person["street"] and person["postal_code"] and person["city"] and person["province"] and person["tel"]
    exists_form_data = form_data["name"] and form_data["surname"] and form_data["email"] and form_data["street"] and form_data["postal_code"] and form_data["city"] and form_data["province"] and form_data["tel"] and form_data["op_codes"]
    if exists_personal_info:
        context = dict(person=person)

    if exists_form_data:
        om = OrderModel(name=person["name"],surname=form_data["surname"],email=form_data["email"],street=form_data["street"],postal_code=form_data["postal_code"],city=form_data["city"],province=form_data["province"],tel=form_data["tel"],payment_method=form_data["payment_method"],credit_card_number=form_data["ccn"],ccv=form_data["ccv"],total_cost=form_data["total_cost"])
        om.save()
        for c,p in form_data["op_codes"].items():
            op = OrderedProductModel(order_id=OrderModel.objects.get(order_id=om.order_id),code=c,pieces=p)
            op.save()

    return render(request,template_name,context)