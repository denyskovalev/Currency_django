from rest_framework.routers import DefaultRouter

from api import views
from django.urls import path

app_name = 'api'

router = DefaultRouter()
router.register('rates', views.RateViewSet, basename='rate')

urlpatterns = [

    path('sources/', views.SourceListView.as_view(), name='sources')
    # for rate CRUD
    # path('rates/', views.RatesView.as_view(), name='rates'),
    # path('rates/<int:pk>/', views.RateDetailsView.as_view(), name='rates-details'),

]

urlpatterns += router.urls
