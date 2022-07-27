from django.db import models
# Create your models here.


class Rate(models.Model):

    base_currency_type = models.CharField(max_length=3)
    currency_type = models.CharField(max_length=3)
    sale = models.DecimalField(max_digits=10, decimal_places=4)  # 999999.9999
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):

    mail_id = models.DecimalField(max_digits=10, decimal_places=4)
    email_from = models.EmailField(max_length=64)
    email_to = models.EmailField(max_length=64)
    subject = models.CharField(max_length=32)
    message = models.TextField(max_length=999)
    date_message = models.DateTimeField(auto_now_add=True)
