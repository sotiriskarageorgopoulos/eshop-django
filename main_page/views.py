from django.shortcuts import render

# Create your views here.

def main_page_view(request):
    template_name="base.html"
    return render(request,template_name,{})
