from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from currency.tasks import send_contact_us_email
from currency.models import Rate, Source, ContactUs
from api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer


# # Rate CRUD
# class RatesView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
#
#
# class RateDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer

class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class SourceListView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    
    def create(self, request, *args, **kwargs):
        send_contact_us_email.delay(request.data['subject'], request.data['email_from'])
        return super(ContactUsViewSet, self).create(request, *args, **kwargs)
