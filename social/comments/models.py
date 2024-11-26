from django.contrib.auth.models import User
from django.db import models
from posts.models import Post
import uuid
from events.models import Event_post

# Create your models here.

class Post_comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created']

class Event_comment(models.Model):
    event_post = models.ForeignKey(Event_post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

