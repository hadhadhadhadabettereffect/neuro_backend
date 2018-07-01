from django.db import models

from ordered_model.models import OrderedModel


class StoryPage(OrderedModel):
    PAGE_TYPES = ["text", "slider"]
    page_type = models.IntegerField(
        choices=list(enumerate(PAGE_TYPES, 1)),
        default=0)
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True)
    image_a = models.ImageField(upload_to="images", blank=True, null=True)
    image_b = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.title
