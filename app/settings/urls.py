
from django.contrib import admin
from django.urls import path

from currency.views import contact_us, rate_list, index_page, create_rate_list, update_rate_list, rate_details, rate_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),

    # Rate list
    path('rate/list/', rate_list),
    path('rate/create/', create_rate_list),
    path('rate/update/<int:rate_id>/', update_rate_list),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/delete/<int:rate_id>/', rate_delete),

    # Contact us
    path('contact-us/', contact_us),
]
