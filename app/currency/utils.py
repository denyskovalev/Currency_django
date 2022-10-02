from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
import datetime

# Create utils


# Utils for Round numbers to normal mode
from decimal import Decimal


def to_decimal(value: str, precision: int = 4) -> int:
    return round(Decimal(value), precision)


# Utils for middleware


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Mixin
class IsSuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return JsonResponse(
            {'message': 'Only superuser can update/delete Rate`s!'}
        )


# Utils for avatar source create
def source_avatar(instance, filename):
    return 'bank_icons/{0}/{1}'.format(instance.code_name, filename)


# Utils for parser archive private bank
def get_current_day(date):
    return date


def get_previous_day(date):
    previous_day = date - datetime.timedelta(1)
    return previous_day


def get_str_day(date):
    year = date.timetuple()[0]
    month = date.timetuple()[1]
    day = date.timetuple()[2]
    return f"{day}.{month}.{year}"
