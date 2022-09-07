
from currency import consts
from django.db import models


class CurrencyTypes(models.TextChoices):
    CURRENCY_TYPE_UAH = 'UAH', 'Hryvnia'
    CURRENCY_TYPE_USD = 'USD', 'Dollar'
    CURRENCY_TYPE_EUR = 'EUR', 'Euro'
    CURRENCY_TYPE_BTC = 'BTC', 'BitCoin'
    CURRENCY_TYPE_GBP = 'GBP', 'Pound Sterling'


class Sources(models.TextChoices):
    SOURCE_PRIVATBANK = consts.CODE_NAME_PRIVATBANK, 'Private Bank'
    CODE_NAME_PRIVATBANK = consts.CODE_NAME_MONOBANK, 'Monobank'
