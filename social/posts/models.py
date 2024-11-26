from django.db import models
import uuid

class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField(max_length=10000, blank=False, null=False)
    post_image = models.ImageField(upload_to='post_images', blank=True, null=True, default='post_images/default.png"')
    youtube_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
