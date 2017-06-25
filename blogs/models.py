from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify
from products.models import ProductCategory


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User)
    likes = models.IntegerField(default=0)
    slug = models.CharField(blank=True, max_length=150)
    category = models.ForeignKey(to=ProductCategory, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Comment(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.email
