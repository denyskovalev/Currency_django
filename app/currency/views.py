
from django.shortcuts import render
from currency.models import Rate, ContactUs


def index_page(request):
    return render(request, 'index.html')


def rate_list(request):

    context = {
        'rate_list': Rate.objects.all(),
    }

    return render(request, 'rate_list.html', context=context)


def contact_us(request):

    context = {
        'contact_us': ContactUs.objects.all(),
    }

    return render(request, 'contact_us.html', context=context)
