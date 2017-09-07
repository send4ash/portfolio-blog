from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone #Imports time zone utility; needed for sorting posts
from django.contrib.auth.decorators import login_required

from .models import Post, Comment # Imports Post and Comment model
from .forms import PostForm, CommentForm #Imports PostForm and CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # QuerySet for sorting published posts by created date
    return render(request, 'blog/post_list.html', {'posts': posts})  #Puts together post list using templates using data saved in "posts"

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns 404 error if post not found
    return render(request, 'blog/post_detail.html', {'post': post}) # Puts together post detail using template and data saved in "post"

@login_required
def post_new(request):
    if request.method == "POST": #If posting form data for the first time, need a blank form
        form = PostForm(request.POST)
        if form.is_valid(): # If all required fields satifised and correct values
            post = form.save(commit=False) #Preserves changes to post
            post.author = request.user  #Adds author
            post.save() #Saves form data
            return redirect('post_detail', pk=post.pk) # Goes to post detail page after submitted
    else: #Displays form (no user action occuring)
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form}) #Passes PostForm() into post_edit template

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns 404 error if post not found
    if request.method == "POST": #If posting form data for the first time, need a blank form
        form = PostForm(request.POST, instance=post) # Requested post saved in "instance"
        if form.is_valid(): # If all required fields satifised and correct values
            post = form.save(commit=False) #Preserves changes to post
            post.author = request.user  #Adds author
            post.save() #Saves form data
            return redirect('post_detail', pk=post.pk) # Goes to post detail page after submitted
    else: #Displays form (no user action occuring)
        form = PostForm(instance=post) # Opens post form with requested post data saved in "instance"
    return render(request, 'blog/post_edit.html', {'form': form}) #Passes PostForm() into post_edit

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') # Orders unpublished posts by creation date
    return render(request, 'blog/post_draft_list.html', {'posts': posts}) # Puts together draft post list using template and data saved in "posts"

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns 404 error if post not found
    post.publish() # Publishes post
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk) # Returns 404 error if post not found
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
