from django.shortcuts import render
from django.utils import timezone
from comments.forms import CommentsForm
from comments.models import CommentsModel

# Create your views here.
def comments_view(request):
    comment_form = CommentsForm(request.POST or None)
    if comment_form.is_valid():
        comment_form.cleaned_data["date"] = timezone.now()
        comment_form.instance.date = comment_form.cleaned_data["date"]
        comment_form.save()
        comment_form = CommentsForm()
    comments = CommentsModel.objects.order_by('-date')#with - order in descending order
    template_name="comments.html"
    context = dict(commentForm=comment_form,comments=comments)
    return render(request,template_name,context)