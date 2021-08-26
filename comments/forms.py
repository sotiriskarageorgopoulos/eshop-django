from django import forms
from comments.models import CommentsModel

class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ["username","email","comment","date"]

    def __init__(self,*args,**kwargs):
        super(CommentsForm,self).__init__(*args,**kwargs)
        self.fields['date'].widget.attrs['class'] = "dont-display-comment-date-form"
        self.fields['username'].widget.attrs['class'] = "comments-field"
        self.fields['comment'].widget.attrs['class'] = "comments-field"
        self.fields['email'].widget.attrs['class'] = "comments-field"