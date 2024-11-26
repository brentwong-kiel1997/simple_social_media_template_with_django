from .models import Event, Event_post
from django.forms import ModelForm, CharField, Textarea, ImageField, DateField


class EventForm(ModelForm):
    event_name = CharField(required=True)
    event_pic = ImageField(required=True)
    class Meta:
        model = Event
        fields = ['event_name', 'event_pic']


class Event_postForm(ModelForm):

    event_post_title = CharField(required=True)
    post = CharField(required=True, widget=Textarea)
    event_post_pic = ImageField(required=True)
    available_date = DateField(required=True)

    class Meta:
        model = Event_post
        fields = ['event_post_title', 'post', 'event_yt_url', 'event_post_pic', 'available_date']
