
from django.contrib import admin
from django.urls import path

from currency.views import generate_password, hello_world, contact_us, rate_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-password/', generate_password),
    path('hello/', hello_world),
    path('contact-us/', contact_us),
    path('rate/list/', rate_list)
]
