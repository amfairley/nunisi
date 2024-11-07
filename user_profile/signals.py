from django.dispatch import receiver

from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        # For a new user
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
