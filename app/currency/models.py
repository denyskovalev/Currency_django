
from currency.utils import source_avatar
from django.db import models
from currency.model_choices import CurrencyTypes, Sources


class Source(models.Model):

    source_name = models.CharField(
        max_length=16, unique=True,
        choices=Sources.choices
    )
    source_url = models.URLField()
    code_name = models.CharField(max_length=16, unique=True, default='')
    avatar = models.FileField(upload_to=source_avatar)
    created = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):

    # def get_{field_name}_display() if field has choices
    base_currency_type = models.CharField(
        max_length=3,
        choices=CurrencyTypes.choices,
        default=CurrencyTypes.CURRENCY_TYPE_USD
    )
    currency_type = models.CharField(
        max_length=3,
        choices=CurrencyTypes.choices,
        default=CurrencyTypes.CURRENCY_TYPE_UAH
    )
    sale = models.DecimalField(max_digits=10, decimal_places=4)  # 999999.9999
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):

    email_from = models.EmailField(max_length=64)
    email_to = models.EmailField(max_length=64)
    subject = models.CharField(max_length=32)
    message = models.TextField(max_length=999)
    date_message = models.DateTimeField(auto_now_add=True)


class ResponseLog(models.Model):

    response_time = models.DecimalField(max_digits=10, decimal_places=8)
    request_method = models.CharField(max_length=32)
    query_params = models.CharField(max_length=255)
    ip_client = models.CharField(max_length=32)
    path = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
