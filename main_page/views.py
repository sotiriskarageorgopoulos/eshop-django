from django.shortcuts import render
from main_page.forms import SearchForm,ContactUsForm
# Create your views here.

def main_page_view(request):
    search_form = SearchForm(request.POST or None)
    contact_us_form = ContactUsForm(request.POST or None)
    if search_form.is_valid():
        search_term = search_form.cleaned_data["search"]
        print(search_term)
        search_form = SearchForm()
        return render(request,"clothes_list.html",{})
    if contact_us_form.is_valid():
        contact_us_form.save()
        contact_us_form = ContactUsForm()
    context = dict(searchForm=search_form,contactUsForm=contact_us_form)
    context["carousel_img"] = ["images/first_carousel.jpg","images/second_carousel.jpg","images/third_carousel.jpg"]
    template_name="main_page.html"
    return render(request,template_name,context)
