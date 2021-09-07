from django.shortcuts import render
from clothes.models import (ClothesModel,ClothesDetailsModel,ShoesModel,ShoesDetailsModel)
from django.db.models import Q,Min
from clothes.models import (sizes,colors)
# Create your views here.
def filter_clothes_by_price(until_price,category):
    return ClothesModel.objects.filter(Q(price__lte=until_price) & Q(category=category))

def filter_clothes_by_color(color,query_set):
    clothes_details = ClothesDetailsModel.objects.all()
    clothes_codes_with_color = set([c.code for c in clothes_details if c.color == color])
    clothes_with_color = list()
    for c in clothes_codes_with_color:
        for q in query_set:
            if q.code == c.code:
                clothes_with_color.append(q)
        
    return clothes_with_color 

def filter_clothes_by_size(size,query_set):   
    clothes_details = ClothesDetailsModel.objects.all()
    clothes_code_with_size = set([c.code for c in clothes_details if c.size == size and c.availability == True])
    clothes_with_size = list()
    for s in clothes_code_with_size:
        for q in query_set:
            if q.code == s.code:
                clothes_with_size.append(q)
    return clothes_with_size

def filter_shoes_by_price(until_price):
    return ShoesModel.objects.filter(Q(price__lte=until_price))

def filter_shoes_by_color(color,query_set):
    shoes_details = ShoesDetailsModel.objects.all()
    shoes_codes_with_color = set([s.code for s in shoes_details if s.color == color])
    shoes_with_color = list()
    for s in shoes_codes_with_color:
        for q in query_set:
            if q.code == s.code:
                shoes_with_color.append(q)
        
    return shoes_with_color 

def filter_shoes_by_size(size,query_set):
    shoes_details = ShoesDetailsModel.objects.all()
    shoes_code_with_size = set([s.code for s in shoes_details if s.size_number == size and s.availability == True])
    shoes_with_size = list()
    for s in shoes_code_with_size:
        for q in query_set:
            if q.code == s.code:
                shoes_with_size.append(q)
    return shoes_with_size

def t_shirts_view(request):
    template_name = "clothes.html"
    until_price = request.POST.get('slider-price')
    color = request.POST.get('color')
    size = request.POST.get('size')
    t_shirts = ClothesModel.objects.filter(category="t-shirt")
    max_price = ClothesModel.objects.filter(category="t-shirt").latest('price').price

    if until_price is not None:
        t_shirts = filter_clothes_by_price(until_price,"t-shirt")
    
    if color is not None: 
        t_shirts = filter_clothes_by_color(color,t_shirts).copy()
    
    if size is not None:
        t_shirts = filter_clothes_by_size(size,t_shirts).copy()

    context = dict(heading='T-shirts',path_name="t_shirt",clothes=t_shirts,sizes=sizes,colors=colors,max_price=max_price)
    return render(request,template_name,context)

def pants_view(request):
    template_name = "clothes.html"
    until_price = request.POST.get('slider-price')
    color = request.POST.get('color')
    size = request.POST.get('size')
    pants = ClothesModel.objects.filter(category="pants")
    max_price = ClothesModel.objects.filter(category="pants").latest('price').price

    if until_price is not None:
        pants = filter_clothes_by_price(until_price,"pants")
    
    if color is not None:
        pants = filter_clothes_by_color(color,pants).copy()

    if size is not None:
        pants = filter_clothes_by_size(size,pants).copy()

    context = dict(heading="Pants",path_name="pant",clothes=pants,sizes=sizes,colors=colors,max_price=max_price)
    return render(request,template_name,context)

def jackets_view(request):
    template_name = "clothes.html"
    until_price = request.POST.get('slider-price')
    color = request.POST.get('color')
    size = request.POST.get('size')
    jackets = ClothesModel.objects.filter(category="jackets")
    max_price = ClothesModel.objects.filter(category="jackets").latest("price").price

    if until_price is not None:
        jackets = filter_clothes_by_price(until_price,"jackets")
    
    if color is not None:
        jackets = filter_clothes_by_color(color,jackets).copy()

    if size is not None:
        jackets = filter_clothes_by_size(size,jackets).copy()

    context = dict(heading="Jackets",path_name="jacket",clothes=jackets,sizes=sizes,colors=colors,max_price=max_price)
    return render(request,template_name,context)

def jeans_view(request):
    template_name = "clothes.html"
    until_price = request.POST.get('slider-price')
    color = request.POST.get('color')
    size = request.POST.get('size')
    jeans = ClothesModel.objects.filter(category="jeans")
    max_price = ClothesModel.objects.filter(category="jeans").latest("price").price

    if until_price is not None:
        jeans = filter_clothes_by_price(until_price,"jeans")
    
    if color is not None:
        jeans = filter_clothes_by_color(color,jeans).copy()

    if size is not None:
        jeans = filter_clothes_by_size(size,jeans).copy()
    
    context = dict(heading="Jeans",path_name="jean",clothes=jeans,sizes=sizes,colors=colors,max_price=max_price)
    return render(request,template_name,context)

def shoes_view(request):
    template_name = "shoes.html"
    until_price = request.POST.get('slider-price')
    color = request.POST.get('color')
    size = request.POST.get('slider-size')
    shoes = ShoesModel.objects.all()
    max_price = ShoesModel.objects.all().latest("price").price
    max_size = ShoesDetailsModel.objects.all().latest("size_number").size_number
    min_size = ShoesDetailsModel.objects.annotate(Min("size_number")).first().size_number

    if until_price is not None:
        shoes = filter_shoes_by_price(until_price)

    if color is not None:
        shoes = filter_shoes_by_color(color,shoes).copy()

    if size is not None:
        shoes = filter_shoes_by_size(int(size),shoes).copy()

    context = dict(heading="Shoes",path_name="shoe",shoes=shoes,colors=colors,max_price=max_price,max_size=max_size,min_size=min_size)
    return render(request,template_name,context)

def t_shirt_view(request,code):
    template_name = "cloth.html"
    t_shirt = ClothesModel.objects.filter(code=code).first()
    t_shirt_details = ClothesDetailsModel.objects.filter(code=code)
    context = dict(cloth=t_shirt,cloth_details=t_shirt_details)
    return render(request,template_name,context)

def pant_view(request,code):
    template_name = "cloth.html"
    pant = ClothesModel.objects.filter(code=code).first()
    pant_details = ClothesDetailsModel.objects.filter(code=code)
    context = dict(cloth=pant,cloth_details=pant_details)
    return render(request,template_name,context)

def jacket_view(request,code):
    template_name = "cloth.html"
    jacket = ClothesModel.objects.filter(code=code).first()
    jacket_details = ClothesDetailsModel.objects.filter(code=code)
    context = dict(cloth=jacket,cloth_details=jacket_details)
    return render(request,template_name,context)

def jean_view(request,code):
    template_name = "cloth.html"
    jean = ClothesModel.objects.filter(code=code).first()
    jean_details = ClothesDetailsModel.objects.filter(code=code)
    context = dict(cloth=jean,cloth_details=jean_details)
    return render(request,template_name,context)

def shoe_view(request,code):
    template_name = "shoe.html"
    shoe = ShoesModel.objects.filter(code=code).first()
    shoe_details = ShoesDetailsModel.objects.filter(code=code)
    context = dict(shoe=shoe,shoe_details=shoe_details)
    return render(request,template_name,context)
