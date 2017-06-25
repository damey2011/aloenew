from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    category = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class StandAloneImageUpload(models.Model):
    image = models.ImageField(upload_to='image-uploads')
