from django.db import models

# Create your models here.


class Prices(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    price = models.TextField(null=True)
    max_price = models.TextField(null=True)