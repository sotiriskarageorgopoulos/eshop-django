from django.shortcuts import render
from main_page.forms import SearchForm
# Create your views here.

def main_page_view(request):
    searchForm = SearchForm(request.POST or None)
    if searchForm.is_valid():
        search_term = searchForm.cleaned_data["search"]
        print(search_term)
        searchForm = SearchForm()
        return render(request,"clothes_list.html",{})
    context = dict(searchForm=searchForm)
    context["carousel_img"] = ["images/first_carousel.jpg","images/second_carousel.jpg","images/third_carousel.jpg"]
    template_name="main_page.html"
    return render(request,template_name,context)
