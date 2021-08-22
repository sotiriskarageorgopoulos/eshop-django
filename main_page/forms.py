from django import forms
from main_page.models import SearchModel

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = ['search']
    
    def __init__(self,*args,**kwargs):
        super(SearchForm,self).__init__(*args,**kwargs)
        self.fields['search'].widget.attrs['placeholder'] = "Search here..."