
import requests
from bs4 import BeautifulSoup

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from currency.utils import to_decimal
from currency import model_choices as mch
from currency import consts


# PrivatBank parser
@shared_task
def parse_privatbank():
    from currency.models import Rate, Source
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    response = requests.get(url)
    response.raise_for_status()  # raise error if not ok

    response_data = response.json()

    currency_type_mapper = {
        'UAH': mch.CurrencyTypes.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyTypes.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyTypes.CURRENCY_TYPE_EUR,
        'BTC': mch.CurrencyTypes.CURRENCY_TYPE_BTC,
    }

    # try:
    #     source = Source.objects.get(source_name=source_name)
    # except Source.DoesNotExist:
    #     source = Source.objects.create(source_name=source_name, source_url=url)
    #
    # source, created = Source.objects.get_or_create(
    #     code_name=consts.CODE_NAME_PRIVATBANK,
    #     defaults={'url': url})
    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_PRIVATBANK,
        defaults={'source_url': url, 'source_name': consts.CODE_NAME_PRIVATBANK},
    )[0]

    for rate_data in response_data:
        base_currency_type = rate_data['base_ccy']
        currency_type = rate_data['ccy']

        # Skip unsupported Currencies
        if currency_type not in currency_type_mapper or \
                base_currency_type not in currency_type_mapper:
            continue

        # Convert private bank currencies into our currency type
        sale = to_decimal(rate_data['sale'])
        buy = to_decimal(rate_data['buy'])

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source,
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or \
                latest_rate.sale != sale or \
                latest_rate.buy != buy:
            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


# Parser Monobank
@shared_task
def parse_monobank():
    from currency.models import Rate, Source
    url = 'https://api.monobank.ua/bank/currency'

    response = requests.get(url)
    response.raise_for_status()  # raise error if not ok

    response_data = response.json()

    currency_type_mapper = {
        '980': mch.CurrencyTypes.CURRENCY_TYPE_UAH,
        '840': mch.CurrencyTypes.CURRENCY_TYPE_USD,
        '978': mch.CurrencyTypes.CURRENCY_TYPE_EUR,
        '826': mch.CurrencyTypes.CURRENCY_TYPE_GBP,
    }

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_MONOBANK,
        defaults={'source_url': url, 'source_name': consts.CODE_NAME_MONOBANK},
    )[0]

    for rate_data in response_data:
        base_currency_type = rate_data['currencyCodeA']
        currency_type = rate_data['currencyCodeB']

        # Skip unsupported Currencies
        if str(currency_type) not in currency_type_mapper or \
                str(base_currency_type) not in currency_type_mapper:
            continue

        # Convert private bank currencies into our currency type
        try:
            sale = to_decimal(rate_data['rateSell'])
            buy = to_decimal(rate_data['rateBuy'])
        except KeyError:
            sale = to_decimal(rate_data['rateCross'])
            buy = to_decimal(rate_data['rateCross'])

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=currency_type_mapper[str(base_currency_type)],
                currency_type=currency_type_mapper[str(currency_type)],
                source=source,
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or \
                latest_rate.sale != sale or \
                latest_rate.buy != buy:
            Rate.objects.create(
                base_currency_type=currency_type_mapper[str(base_currency_type)],
                currency_type=currency_type_mapper[str(currency_type)],
                sale=sale,
                buy=buy,
                source=source,
            )


# Parser Vkurse
@shared_task
def parse_vkurse():
    from currency.models import Rate, Source
    url = 'http://vkurse.dp.ua/course.json'

    response = requests.get(url)
    response.raise_for_status()  # raise error if not ok

    response_data = response.json()

    currency_type_mapper = {
        'Dollar': mch.CurrencyTypes.CURRENCY_TYPE_USD,
        'Euro': mch.CurrencyTypes.CURRENCY_TYPE_EUR,
    }

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_VKURSE,
        defaults={'source_url': url, 'source_name': consts.CODE_NAME_VKURSE},
    )[0]

    for rate_data in response_data:
        base_currency_type = mch.CurrencyTypes.CURRENCY_TYPE_UAH
        currency_type = rate_data

        # Skip unsupported Currencies
        if currency_type not in currency_type_mapper:
            continue

        # Convert private bank currencies into our currency type
        try:
            sale = to_decimal(response_data[rate_data]['sale'])
            buy = to_decimal(response_data[rate_data]['buy'])
        except KeyError:
            sale = to_decimal(response_data[rate_data]['sale'])
            buy = to_decimal(response_data[rate_data]['buy'])

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type_mapper[currency_type],
                source=source,
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or \
                latest_rate.sale != sale or \
                latest_rate.buy != buy:
            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type_mapper[currency_type],
                sale=sale,
                buy=buy,
                source=source,
            )


# Parse oshadbank
@shared_task
def parse_oschadbank():
    # bs4
    from currency.models import Rate, Source
    url = 'https://www.oschadbank.ua/currency-rate'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    full_page = requests.get(url, headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = list(soup.findAll('tr', {'class': 'heading-block-currency-rate__table-row'}))

    currency_type_mapper = {
        'USD': mch.CurrencyTypes.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyTypes.CURRENCY_TYPE_EUR,
        'GBP': mch.CurrencyTypes.CURRENCY_TYPE_GBP,
    }

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_OSCHADBANK,
        defaults={'source_url': url, 'source_name': consts.CODE_NAME_OSCHADBANK},
    )[0]

    # select rows with currency info and create rate
    for row in range(len(convert)):

        data_soup = convert[row]
        data_soup_list = list(
            data_soup.findAll('span', {'class': 'heading-block-currency-rate__table-txt body-regular'})
        )

        base_currency_type = mch.CurrencyTypes.CURRENCY_TYPE_UAH
        currency_type = data_soup_list[1].text

        # Skip unsupported Currencies
        if currency_type not in currency_type_mapper:
            continue

        sale = to_decimal(data_soup_list[4].text)
        buy = to_decimal(data_soup_list[3].text)

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source,
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or \
                latest_rate.sale != sale or \
                latest_rate.buy != buy:

            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


# Parse Finance UA
@shared_task
def parse_finance_ua():
    from currency.models import Rate, Source
    # bs4
    url = 'https://finance.ua/ua/currency'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    full_page = requests.get(url, headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = list(soup.findAll('tr', {'class': 'major'}))

    currency_type_mapper = {
        'USD': mch.CurrencyTypes.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyTypes.CURRENCY_TYPE_EUR,
        'GBP': mch.CurrencyTypes.CURRENCY_TYPE_GBP,
    }

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_FINANCE_UA,
        defaults={'source_url': url, 'source_name': consts.CODE_NAME_FINANCE_UA},
    )[0]

    for row in range(len(convert)):

        data_soup = convert[row]
        data_soup_list = data_soup.text.split()

        base_currency_type = mch.CurrencyTypes.CURRENCY_TYPE_UAH
        currency_type = data_soup_list[0]

        if currency_type not in currency_type_mapper:
            continue

        sale = to_decimal(data_soup_list[1])
        buy = to_decimal(data_soup_list[3])

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source,
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or \
                latest_rate.sale != sale or \
                latest_rate.buy != buy:

            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


# Parse Ukrsibbank
@shared_task()
def parse_ukrsibbank():
    # bs4
    from currency.models import Rate, Source
    url = 'https://my.ukrsibbank.com/ru/personal/operations/currency_exchange/'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    full_page = requests.get(url, headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = list(soup.find('table', {'class': 'currency__table'}))
    convert_list = convert[3].findAll('tr', {'class': ''})

    currency_type_mapper = {
        'USD, доллар США': mch.CurrencyTypes.CURRENCY_TYPE_USD,
        'EUR, евро': mch.CurrencyTypes.CURRENCY_TYPE_EUR,
        'GBP, фунт стерлингов': mch.CurrencyTypes.CURRENCY_TYPE_GBP,
    }

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_UKRSIBBANK,
        defaults={'source_url': url, 'source_name': consts.CODE_NAME_UKRSIBBANK},
    )[0]

    # select rows with currency info and create rate
    for row in range(len(convert_list)):

        data_soup = convert_list[row]
        data_soup_list = list(data_soup.findAll('td', {'class': ''}))

        base_currency_type = mch.CurrencyTypes.CURRENCY_TYPE_UAH
        currency_type = data_soup_list[0].text

        # Skip unsupported Currencies
        if currency_type not in currency_type_mapper:
            continue
        else:
            currency_type = currency_type_mapper[currency_type]

        sale = to_decimal(data_soup_list[1].text[7:])
        buy = to_decimal(data_soup_list[2].text[7:])

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source,
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or \
                latest_rate.sale != sale or \
                latest_rate.buy != buy:

            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def send_contact_us_email(subject, from_email):
    email_subject = 'ContactUs from Currency Project'
    body = f'''
            Subject from client: {subject}
            Email: {from_email}
            Wants to contact
                '''

    send_mail(
        email_subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
