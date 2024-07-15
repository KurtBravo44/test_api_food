from rest_framework import serializers

from food.models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional', 'is_publish') # Добавление поля is_publish


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        filtered_foods = [food for food in data['foods'] if food.get('is_publish')]

        # Удаляем поле is_publish из продуктов
        for food in filtered_foods:
            food.pop('is_publish', None)

        # Проверяем, есть ли какие-либо продукты после фильтрации
        if filtered_foods:
            data['foods'] = filtered_foods
            return data
        else:
            return None # Если нет продуктов, удовлетворяющих условию, возвращаем None