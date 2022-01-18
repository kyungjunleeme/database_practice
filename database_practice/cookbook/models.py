from django.db import models

class TempUser(models.Model):
    first_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "temp_user"


class Book(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()


# Create your models here.
