from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'post_image', 'youtube_url']

    title = forms.CharField(required=True)
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4}))
