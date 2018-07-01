from django.db import models

from neuro.singleton.models import SingletonModel


class Services(SingletonModel):
    title = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name_plural = 'Services'


class AgencyService(models.Model):
    group = models.ForeignKey(Services, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
