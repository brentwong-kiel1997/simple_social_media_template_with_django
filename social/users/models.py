# users/models.py
from django.contrib.auth.models import User
from django.db import models
import uuid
from django.core.files.storage import default_storage


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    user_name = models.CharField(max_length=255, blank=True, unique=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        # Only delete the old image if the profile is being updated (i.e., it's not a new object)
        if self.pk:  # Check if the instance already exists (it's an update)
            try:
                old_profile = Profile.objects.get(pk=self.pk)
                if old_profile.profile_image and not self.profile_image:
                    default_storage.delete(old_profile.profile_image.name)
            except Profile.DoesNotExist:
                pass  # In case the profile doesn't exist yet (new object)

        super().save(*args, **kwargs)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipient")
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.sender.username + ' to ' + self.recipient.username

    class Meta:
        ordering = ['is_read','-created']