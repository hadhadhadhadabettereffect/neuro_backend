from django.db import models


class PressImage(models.Model):
    image = models.ImageField(upload_to="images")
    link = models.URLField(blank=True)

class PressQuote(models.Model):
    quote = models.TextField()
    publication = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
