from django.db import models
from ordered_model.models import OrderedModel


class PressItem(OrderedModel):
    PRESS_TYPES = ["quote", "image"]
    name = models.CharField(max_length=200, blank=True)
    item_type = models.IntegerField(
        choices=list(enumerate(PRESS_TYPES, 0)),
        default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    quote = models.TextField(blank=True)
    publication = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)

    class Meta(OrderedModel.Meta):
        pass

class PressImage(models.Model):
    image = models.ImageField(upload_to="images")
    link = models.URLField(blank=True)

class PressQuote(models.Model):
    quote = models.TextField()
    publication = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
