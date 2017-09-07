from django import forms # Django Forms function

from .models import Post, Comment # Post and Comment model

class PostForm(forms.ModelForm):

    class Meta:
        model = Post    # Use Post model to create form
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment # Use Comment model to create form
        fields = ('author', 'text',)
