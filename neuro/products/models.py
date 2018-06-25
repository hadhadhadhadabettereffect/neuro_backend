import os
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from ordered_model.models import OrderedModel

from neuro.settings import Common


class Product(OrderedModel):
    CLOTHING_TYPES = ["dress", "accessory", "jacket", "pants", "top", "shoes"]

    name = models.CharField(max_length=250)
    clothing_type = models.IntegerField(
        choices=list(enumerate(CLOTHING_TYPES, 1)),
        default=0)
    description = models.TextField(blank=True, max_length=500)
    materials = models.TextField(blank=True, max_length=500)
    main_image = models.ImageField(upload_to="photos")
    thumbnail = models.ImageField(upload_to="photos")
    detail_1 = models.ImageField(upload_to="photos")
    detail_2 = models.ImageField(upload_to="photos")
    detail_3 = models.ImageField(upload_to="photos")
    detail_4 = models.ImageField(upload_to="photos")

    ## override save
    ## renaming photos with product id + photo type
    def save(self, *args, **kwargs):
        # saving first to ensure self.id != None
        super(Product, self).save(*args, **kwargs)

        new_name = "photos/{}_m.jpg".format(self.id)
        new_path = os.path.join(Common.MEDIA_ROOT, new_name)
        os.rename(self.main_image.path, new_path)
        self.main_image.name = new_name

        new_name = "photos/{}_t.jpg".format(self.id)
        new_path = os.path.join(Common.MEDIA_ROOT, new_name)
        os.rename(self.thumbnail.path, new_path)
        self.thumbnail.name = new_name

        new_name = "photos/{}_1.jpg".format(self.id)
        new_path = os.path.join(Common.MEDIA_ROOT, new_name)
        os.rename(self.detail_1.path, new_path)
        self.detail_1.name = new_name

        new_name = "photos/{}_2.jpg".format(self.id)
        new_path = os.path.join(Common.MEDIA_ROOT, new_name)
        os.rename(self.detail_2.path, new_path)
        self.detail_2.name = new_name

        new_name = "photos/{}_3.jpg".format(self.id)
        new_path = os.path.join(Common.MEDIA_ROOT, new_name)
        os.rename(self.detail_3.path, new_path)
        self.detail_3.name = new_name

        new_name = "photos/{}_4.jpg".format(self.id)
        new_path = os.path.join(Common.MEDIA_ROOT, new_name)
        os.rename(self.detail_4.path, new_path)
        self.detail_4.name = new_name

        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta(OrderedModel.Meta):
        pass
