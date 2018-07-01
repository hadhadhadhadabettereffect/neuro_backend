from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images')
    name = title = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True, max_length=500)


@receiver
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
