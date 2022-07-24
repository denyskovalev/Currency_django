
from django.contrib import admin
from django.urls import path

from currency.views import generate_password, hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-password/', generate_password),
    path('hello/', hello_world),
]
