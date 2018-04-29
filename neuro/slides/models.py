from django.db import models

from ordered_model.models import OrderedModel


class Service(OrderedModel):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta(OrderedModel.Meta):
        pass