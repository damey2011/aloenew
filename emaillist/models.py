from django.db import models


# Create your models here.
class EmailList(models.Model):
    email = models.EmailField()
