from rest_framework import generics

from food.models import FoodCategory
from food.serializers import FoodListSerializer


class FoodListApiView(generics.ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.all()