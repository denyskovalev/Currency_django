
from django.contrib import admin
from django.urls import path

from currency.views import contact_us, rate_list, index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-us/', contact_us),
    path('rate/list/', rate_list),
    path('', index_page),
]
