from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    image = models.TextField()
    price = models.IntegerField()
    release_data = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)

