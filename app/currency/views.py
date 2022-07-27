
from django.http import HttpResponse
from currency.utils import get_password, get_rate_list, get_contact_us

# Create your views here.


def generate_password(request):
    length = int(request.GET.get('length'))

    password = get_password(length)
    return HttpResponse(password)


def hello_world(request):
    return HttpResponse('Hello world!')


def rate_list(request):

    rate = get_rate_list()
    rate_html = []
    for r in rate:
        rate_html.append(f'<br>{r}</br>')

    return HttpResponse(rate_html)


def contact_us(request):

    cont_us = get_contact_us()
    contact_us_html = []
    for c in cont_us:
        contact_us_html.append(f'<br>{c}</br>')

    return HttpResponse(contact_us_html)
