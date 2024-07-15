from django.urls import path

from food.apps import FoodConfig
from food.views import FoodListApiView

app_name = FoodConfig.name

urlpatterns = [
    path('', FoodListApiView.as_view(), name='food_list')

]