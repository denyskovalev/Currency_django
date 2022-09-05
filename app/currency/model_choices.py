
from django.db import models


class CurrencyTypes(models.TextChoices):
    CURRENCY_TYPE_UAH = 'UAH', 'Hryvnia'
    CURRENCY_TYPE_USD = 'USD', 'Dollar'
    CURRENCY_TYPE_EUR = 'EUR', 'Euro'
    CURRENCY_TYPE_BTC = 'BTC', 'BitCoin'
    CURRENCY_TYPE_GBP = 'GBP', 'Pound Sterling'
