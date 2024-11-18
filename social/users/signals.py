from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            user_name = user.username,
            email=user.email,
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("Profile deleted, user deleted")


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    if created == False:
        profile = instance
        user = profile.user
        user.username = profile.user_name
        user.email = profile.email
        user.save()
