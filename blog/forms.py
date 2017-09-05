from django import forms # Django Forms function

from .models import Post # Post model

class PostForm(forms.ModelForm):

    class Meta:
        model = Post    # Use Post model to create form
        fields = ('title', 'text',)
