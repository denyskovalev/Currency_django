
from django.urls import path
from currency import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'currency'

urlpatterns = [

    # Rate list class:
    path('rate/list/', views.RateListView.as_view(), name='rate_list'),
    path('rate/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/download/', views.DownloadRateView.as_view(), name='rate_download'),
    path('rate/update/<int:pk>/', views.RateUpdateView.as_view(), name='rate_update'),
    path('rate/delete/<int:pk>/', views.RateDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', views.RateDetailsView.as_view(), name='rate_details'),

    # Rest example
    # path('api/example/', views.api_get_rate_list, name='api_example'),

    # Contact us
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),
    path('contact-us/create/', views.ContactUsCreateView.as_view(), name='contact_us_create'),

    # Source
    path('source/show/', views.SourceShowView.as_view(), name='source_show'),
    path('source/create/', views.SourceCreateView.as_view(), name='source_create'),
    path('source/details/<int:pk>/', views.SourceDetailsView.as_view(), name='source_details'),
    path('source/update/<int:pk>/', views.SourceUpdateView.as_view(), name='source_update'),
    path('source/delete/<int:pk>/', views.SourceDeleteView.as_view(), name='source_delete'),

]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
