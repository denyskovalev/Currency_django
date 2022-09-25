
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from api.filters import RateFilter, ContactUsFilter, SourceFilter
from api.pagination import RatePagination
from api.throttles import AnonCurrencyThrottle
from currency.tasks import send_contact_us_email
from currency.models import Rate, Source, ContactUs
from api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = RatePagination

    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'buy', 'sale']
    throttle_classes = [AnonCurrencyThrottle]


class SourceListView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    filterset_class = SourceFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'source_name', 'created']
    throttle_classes = [AnonCurrencyThrottle]


class ContactUsViewSet(ModelViewSet):

    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    filterset_class = ContactUsFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'email_from', 'email_to', 'date_message']
    throttle_classes = [AnonCurrencyThrottle]

    def create(self, request, *args, **kwargs):
        send_contact_us_email.delay(request.data['subject'], request.data['email_from'])
        return super().create(request, *args, **kwargs)
