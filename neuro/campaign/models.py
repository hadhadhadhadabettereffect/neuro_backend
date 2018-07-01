from django.db import models

from neuro.singleton.models import SingletonModel


class Campaign(SingletonModel):
    title = models.CharField(max_length=150, blank=True)
    text = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'contact'


class CampaignImage(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
