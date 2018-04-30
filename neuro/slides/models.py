from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from ordered_model.models import OrderedModel


class Image(models.Model):
    image = models.ImageField(upload_to="images")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class SlideItem(OrderedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta(OrderedModel.Meta):
        pass


class Service(SlideItem):
    pass


class Work(SlideItem):
    class Meta(OrderedModel.Meta):
        verbose_name_plural = "work"