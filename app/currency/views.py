
from django.http import HttpResponse
from currency.utils import get_password

# Create your views here.


def generate_password(request):
    length = int(request.GET.get('length'))

    password = get_password(length)
    return HttpResponse(password)


def hello_world(request):
    return HttpResponse('Hello world!')
