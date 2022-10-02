
from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank, parse_vkurse, parse_monobank


def test_parse_privatbank(mocker):
    # Rate.objects
    response_json = [
        {"ccy": "USD", "base_ccy": "UAH", "buy": "411.00000", "sale": "411.50000"},
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "39.90000", "sale": "40.90000"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "17668.2920", "sale": "19528.1122"},
        {"ccy": "TTT", "base_ccy": "USD", "buy": "17668.2920", "sale": "19528.1122"},
    ]

    initial_rate_count = Rate.objects.count()  # 6
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: response_json),
    )
    parse_privatbank()
    assert Rate.objects.count() == initial_rate_count + 3

    parse_privatbank()
    assert Rate.objects.count() == initial_rate_count + 3


def test_parse_vkurse(mocker):
    # Rates objects
    response_json = {
        "Dollar": {"buy": "41.60", "sale": "42.20"},
        "Euro": {"buy": "40.00", "sale": "40.50"},
        "Pln": {"buy": "8.15", "sale": "8.65"}
    }

    Rate.objects.all().delete()

    initial_rate_count = Rate.objects.count()  # 6
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: response_json),
    )

    parse_vkurse()
    assert Rate.objects.count() == initial_rate_count + 2

    parse_vkurse()
    assert Rate.objects.count() == initial_rate_count + 2


def test_parse_monobank(mocker):
    response_json = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1664658609, "rateBuy": 36.65, "rateSell": 37.9507},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1664658609, "rateBuy": 35.65, "rateSell": 37.4504},
        {"currencyCodeA": 933, "currencyCodeB": 980, "date": 1664717945, "rateCross": 15.616},
        {"currencyCodeA": 826, "currencyCodeB": 980, "date": 1664717945, "rateCross": 15.616}
    ]

    Rate.objects.all().delete()

    initial_rate_count = Rate.objects.count()  # 6
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: response_json),
    )

    parse_monobank()
    assert Rate.objects.count() == initial_rate_count + 3

    parse_monobank()
    assert Rate.objects.count() == initial_rate_count + 3
