from django.db import models

# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# ...

class FlexCategory(models.Model):
    name = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Hero(models.Model):
    name = models.CharField(max_length=100)
    flex_category = GenericRelation(FlexCategory, related_query_name='flex_category')
    # ...


class Villain(models.Model):
    name = models.CharField(max_length=100)
    flex_category = GenericRelation(FlexCategory, related_query_name='flex_category')
    # ...