from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create utils


# Utils for Round numbers to normal mode
from decimal import Decimal


def to_decimal(value: str, precision: int = 4) -> int:
    return round(Decimal(value), precision)


# Utils for middleware
from django.http import JsonResponse


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
