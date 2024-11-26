from django.db import models
import uuid


# Create your models here.


class Event(models.Model):
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    event_pic = models.ImageField(upload_to='event_pics', blank=True, default='event_pics/default.png')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    number_of_posts = models.IntegerField(default=0)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['-updated', '-created']


class Event_post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='event_posts', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='posts', on_delete=models.CASCADE)
    event_post_title = models.CharField(max_length=100)
    post = models.TextField()
    event_yt_url = models.URLField(blank=True)
    event_post_pic = models.ImageField(upload_to='event_post_pics', blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_post_title

    class Meta:
        ordering = ['-created']
