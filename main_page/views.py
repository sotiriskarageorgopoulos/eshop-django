from django.shortcuts import render
from main_page.forms import SearchForm,ContactUsForm
from clothes.models import (ClothesModel,ShoesModel,ShoesDetailsModel,ClothesDetailsModel)
from django.db.models import Q
from itertools import chain
# Create your views here.
def search(search_term):
    filtered_clothes = ClothesModel.objects.filter(Q(brand__icontains=search_term) | Q(model__icontains=search_term) | Q(category__icontains=search_term))
    filtered_shoes = ShoesModel.objects.filter(Q(brand__icontains=search_term))
    filtered_shoes_details = list(ShoesDetailsModel.objects.filter(Q(color__icontains=search_term)).values('code'))
    filtered_clothes_details = list(ClothesDetailsModel.objects.filter(Q(color__icontains=search_term) | Q(size__icontains=search_term)).values('code'))
        
    clothes_code = set([c.code for c in filtered_clothes])
    shoes_code = set([s.code for s in filtered_shoes])
    shoes_details_code = set([sd["code"] for sd in filtered_shoes_details])
    clothes_details_code = set([cd["code"] for cd in filtered_clothes_details])

    searched_codes = list(set(chain(clothes_code,shoes_code,shoes_details_code,clothes_details_code)))
    search_results = list()
    clothes = ClothesModel.objects.all()
    shoes = ShoesModel.objects.all()

    for sc in searched_codes:
        for c in clothes:
            if sc == c.code:
               search_results.append(c)

    for sc in searched_codes:
        for s in shoes:
            if sc == s.code:
                search_results.append(s)
    return search_results

def main_page_view(request):
    search_form = SearchForm(request.POST or None)
    contact_us_form = ContactUsForm(request.POST or None)
    
    if search_form.is_valid():
        search_term = search_form.cleaned_data["search"]
        search_results = search(search_term).copy()
        context = dict(search_results=search_results,path_name='searched_item')
        template_name = "searching_list.html"
        return render(request,template_name,context)

    if contact_us_form.is_valid():
        contact_us_form.save()
        contact_us_form = ContactUsForm()

    context = dict(searchForm=search_form,contactUsForm=contact_us_form)
    template_name="main_page.html"
    return render(request,template_name,context)


def searched_item_view(request,code):
    template_name = "searching_list_item.html"
    cloth = ClothesModel.objects.filter(code=code).first()
    shoe = ShoesModel.objects.filter(code=code).first()
    context = dict()

    if cloth is not None:
        cloth_details = ClothesDetailsModel.objects.filter(code=code)
        context = dict(s_item=cloth,s_item_details=cloth_details)
    elif shoe is not None:
        shoe_details = ShoesDetailsModel.objects.filter(code=code)
        context = dict(s_item=shoe,s_item_details=shoe_details)   
    
    return render(request,template_name,context)