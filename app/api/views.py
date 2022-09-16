from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

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
