from django.db import models

from neuro.singleton.models import SingletonModel


class Contact(SingletonModel):
    header = models.CharField(max_length=150, blank=True)
    message = models.TextField(max_length=500, blank=True)
    email = models.EmailField(default='contact@neuro-studio.com')
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'contact'
