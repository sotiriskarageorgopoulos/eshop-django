from django import forms
from main_page.models import SearchModel,ContactUsModel

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = ['search']
    
    def __init__(self,*args,**kwargs):
        super(SearchForm,self).__init__(*args,**kwargs)
        self.fields['search'].widget.attrs['placeholder'] = "Search here..."

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['name','surname','email','subject','message']

    def __init__(self,*args,**kwargs):
        super(ContactUsForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = "contact-us-field"
        self.fields['surname'].widget.attrs['class'] = "contact-us-field"
        self.fields['email'].widget.attrs['class'] = "contact-us-field"
        self.fields['subject'].widget.attrs['class'] = "contact-us-field"
        self.fields['message'].widget.attrs['class'] = "contact-us-message"