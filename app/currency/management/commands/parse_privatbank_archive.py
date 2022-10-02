import datetime

import requests
from django.core.management.base import BaseCommand
from currency.models import Rate, Source
from currency.utils import get_previous_day, get_str_day, to_decimal
from currency import model_choices as mch
from currency import consts
from django.utils.timezone import make_aware


class Command(BaseCommand):
    help = 'Closes the specified pool for voting'

    def handle(self, *args, **options):

        # Set current day
        base_date = datetime.date.today()
        time = datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
        current_day = datetime.datetime.combine(base_date, time)
        # or this for test, 2014/03/31 last available day
        # current_day = get_current_day(datetime.datetime(
        #     year=2014, month=4, day=1,
        #     hour=0, minute=0, second=0, microsecond=0, tzinfo=None))

        # Set mapper
        currency_type_mapper = {
            'UAH': mch.CurrencyTypes.CURRENCY_TYPE_UAH,
            'USD': mch.CurrencyTypes.CURRENCY_TYPE_USD,
            'EUR': mch.CurrencyTypes.CURRENCY_TYPE_EUR,
            'BTC': mch.CurrencyTypes.CURRENCY_TYPE_BTC,
        }
        # Set source
        source = Source.objects.get_or_create(
            code_name=consts.CODE_NAME_PRIVATBANK,
            defaults={'source_url': 'https://api.privatbank.ua/p24api/exchange_rates?json&date=',
                      'source_name': consts.CODE_NAME_PRIVATBANK},
        )[0]

        while True:

            # Get str for url
            str_day = get_str_day(current_day)

            # Url
            url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={str_day}'

            # Get response
            response = requests.get(url)
            response.raise_for_status()  # raise error if not ok
            response_data = response.json()

            # stop parsing if archive for this day empty
            if not response_data['exchangeRate']:
                break

            # cycle for creating rates
            for rate_data in response_data['exchangeRate']:
                base_currency_type = rate_data['baseCurrency']

                # Try to setup currency types
                # Some rate in rate_data nat have 'currency' key
                try:
                    currency_type = rate_data['currency']
                except KeyError:
                    continue

                # Skip unsupported Currencies
                if currency_type not in currency_type_mapper or \
                        base_currency_type not in currency_type_mapper or \
                        currency_type == base_currency_type:
                    continue

                # Convert private bank currencies into our currency type
                sale = to_decimal(rate_data['saleRateNB'])
                buy = to_decimal(rate_data['purchaseRateNB'])

                try:
                    latest_rate = Rate.objects.filter(
                        base_currency_type=base_currency_type,
                        currency_type=currency_type,
                        source=source,
                        created=make_aware(current_day),
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
                        created=make_aware(current_day),
                    )
            # Set previous day to current day for next cycle
            current_day = get_previous_day(current_day)
