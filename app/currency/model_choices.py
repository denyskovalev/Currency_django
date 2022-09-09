
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
    SOURCE_MONOBANK = consts.CODE_NAME_MONOBANK, 'Monobank'
    SOURCE_VKURSE = consts.CODE_NAME_VKURSE, 'Vkurse'
    SOURCE_OSCHADBANK = consts.CODE_NAME_OSCHADBANK, 'Oschadbank'
    SOURCE_FINANCE_UA = consts.CODE_NAME_FINANCE_UA, 'Finance.ua'
    SOURCE_UKRSIBBANK = consts.CODE_NAME_UKRSIBBANK, 'Ukrsibbank'
