
from django.db import models


class CurrencyTypes(models.TextChoices):
    CURRENCY_TYPE_UAH = 'UAH', 'Hryvnia'
    CURRENCY_TYPE_USD = 'USD', 'Dollar'
    CURRENCY_TYPE_EUR = 'EUR', 'Euro'
    CURRENCY_TYPE_KZH = 'KZH', 'Kazakh'
    CURRENCY_TYPE_CZK = 'CZK', 'Czech crown'
    CURRENCY_TYPE_JPY = 'JPY', 'Yen'
    CURRENCY_TYPE_CHF = 'CHF', 'Swiss francs'
    CURRENCY_TYPE_BTC = 'BTC', 'BitCoin'
