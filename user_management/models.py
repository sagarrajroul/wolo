from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.IntegerField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-id']
