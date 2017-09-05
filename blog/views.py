from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone #Imports time zone utility; needed for sorting posts

from .models import Post # Imports Post model
from .forms import PostForm #Imports PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # QuerySet for sorting published posts by created date
    return render(request, 'blog/post_list.html', {'posts': posts})  #Puts together post list using templates using data saved in "posts"

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns 404 error if post not found
    return render(request, 'blog/post_detail.html', {'post': post}) # Puts together post detail using template and data saved in "post"

def post_new(request):
    if request.method == "POST": #If posting form data for the first time, need a blank form
        form = PostForm(request.POST)
        if form.is_valid(): # If all required fields satifised and correct values
            post = form.save(commit=False) #Preserves changes to post
            post.author = request.user  #Adds author
            post.published_date = timezone.now() #Adds publish date and time
            post.save() #Saves form data
            return redirect('post_detail', pk=post.pk) # Goes to post detail page after submitted
    else: #Displays form (no user action occuring)
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form}) #Passes PostForm() into post_edit template


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns 404 error if post not found
    if request.method == "POST": #If posting form data for the first time, need a blank form
        form = PostForm(request.POST, instance=post) # Requested post saved in "instance"
        if form.is_valid(): # If all required fields satifised and correct values
            post = form.save(commit=False) #Preserves changes to post
            post.author = request.user  #Adds author
            post.published_date = timezone.now() #Adds publish date and time
            post.save() #Saves form data
            return redirect('post_detail', pk=post.pk) # Goes to post detail page after submitted
    else: #Displays form (no user action occuring)
        form = PostForm(instance=post) # Opens post form with requested post data saved in "instance"
    return render(request, 'blog/post_edit.html', {'form': form}) #Passes PostForm() into post_edit
