
from django.shortcuts import render
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

    # cont_us = get_contact_us()
    # contact_us_html = []
    # for c in cont_us:
    #     contact_us_html.append(f'<br>{c}</br>')

    context = {
        'message': 'HELLO TEXT'
        }

    return render(request, 'rate_list.html', context=context)


def contact_us(request):

    cont_us = get_contact_us()
    contact_us_html = []
    for c in cont_us:
        contact_us_html.append(f'<br>{c}</br>')

    return HttpResponse(str(contact_us_html))
