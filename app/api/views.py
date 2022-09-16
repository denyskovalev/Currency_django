
from rest_framework.viewsets import ModelViewSet

from currency.models import Rate
from api.serializers import RateSerializer


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
