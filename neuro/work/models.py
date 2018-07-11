import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from neuro.settings import Common
from ordered_model.models import OrderedModel


class Project(OrderedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')


# @receiver(post_save, sender=Project)
# def rewrite_html(sender, instance, **kwargs):
#     projects = Project.objects.all()
#     content = render_to_string('work.html', { 'projects': projects })
#     with open(os.path.join(Common.STATIC_ROOT, 'work.html'), 'w') as f:
#             f.write(content)
