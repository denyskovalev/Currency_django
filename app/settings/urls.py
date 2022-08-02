
from django.contrib import admin
from django.urls import path

from currency.views import contact_us, rate_list, index_page, create_rate_list,\
    update_rate_list, rate_details, rate_delete, source_show, source_create, \
    source_details, source_update, source_delete

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

    # Source
    path('source/show/', source_show),
    path('source/create/', source_create),
    path('source/details/<int:source_id>/', source_details),
    path('source/update/<int:source_id>/', source_update),
    path('source/delete/<int:source_id>/', source_delete),
]
