from django.db import models
from django.conf import settings

# Create your models here.

class Posting(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    content = models.TextField()


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='recomment', null=True)

# https://himanmengit.github.io/django/2018/02/06/DjangoModels-07-ManyToMany-Self-Symmetrical.html
# 내일 하긔!