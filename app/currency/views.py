
from django.shortcuts import render
from currency.models import Rate, ContactUs


# Index functions
def index_page(request):
    return render(request, 'index.html')


# Rate list functions
def rate_list(request):

    context = {
        'rate_list': Rate.objects.all(),
    }

    return render(request, 'rate_list.html', context=context)


def create_rate_list(request):

    context = {

    }

    return render(request, 'create_rate_list.html', context=context)


# Contact us functions
def contact_us(request):

    context = {
        'contact_us': ContactUs.objects.all(),
    }

    return render(request, 'contact_us.html', context=context)
