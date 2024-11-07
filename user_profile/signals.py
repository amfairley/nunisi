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
        # For a new user create a UserProfile and automatically set email
        UserProfile.objects.create(user=instance, email=instance.email)
    # Existing users: just save the profile
    instance.userprofile.save()
