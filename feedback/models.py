from django.db import models


# Create your models here.
class FeedBack(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
