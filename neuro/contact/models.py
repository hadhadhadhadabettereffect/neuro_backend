import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from neuro.settings import Common
from neuro.singleton.models import SingletonModel


class Contact(SingletonModel):
    header = models.CharField(max_length=150, blank=True)
    message = models.TextField(max_length=500, blank=True)
    email = models.EmailField(default='contact@neuro-studio.com')
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'contact'


@receiver(post_save, sender=Contact)
def rewrite_html(sender, instance, **kwargs):
    content = render_to_string('contact.html', Contact.load().__dict__)
    with open(os.path.join(Common.STATIC_ROOT, 'contact.html'), 'w') as f:
            f.write(content)
