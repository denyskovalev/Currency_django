
from django.contrib import admin
from django.urls import path

from currency.views import contact_us, rate_list, index_page, create_rate_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),

    # Rate list
    path('rate/list/', rate_list),
    path('rate/create/', create_rate_list),

    # Contact us
    path('contact-us/', contact_us),
]
