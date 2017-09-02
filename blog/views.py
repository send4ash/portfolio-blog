from django.shortcuts import render
from django.utils import timezone #Imports time zone utility; needed for sorting posts
from .models import Post # Imports Post model

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # QuerySet for sorting published posts by created date
    return render(request, 'blog/post_list.html', {'posts': posts})  #Puts together template using posts
