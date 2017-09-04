from django.shortcuts import render, get_object_or_404
from django.utils import timezone #Imports time zone utility; needed for sorting posts
from .models import Post # Imports Post model

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # QuerySet for sorting published posts by created date
    return render(request, 'blog/post_list.html', {'posts': posts})  #Puts together post list using templates using data saved in "posts"

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns 404 error if post not found
    return render(request, 'blog/post_detail.html', {'post': post}) # Puts together post detail using template and data saved in "post"
