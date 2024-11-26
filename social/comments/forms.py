from .models import Post_comment, Event_comment
from django.forms import ModelForm

class Post_commentForm(ModelForm):
    class Meta:
        model = Post_comment
        fields = ['comment']

class Event_commentForm(ModelForm):
    class Meta:
        model = Event_comment
        fields = ['comment']