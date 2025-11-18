from rest_framework import serializers
from .models import User, Learning_materials, Pay_materials, Rating, Tag

class learning_material_serializer(serializers.ModelSerializer):
    class Meta:
        model = Learning_materials
        fields = '__all__'

class Pay_materials_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pay_materials
        fields = '__all__'