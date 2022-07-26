from django.db import models
# Create your models here.


class Rate(models.Model):

    base_currency_type = models.CharField(max_length=3)
    currency_type = models.CharField(max_length=3)
    sale = models.DecimalField(max_digits=10, decimal_places=4)  # 999999.9999
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.CharField(max_length=64)
    created = models.DateTimeField(auto_created=True)

