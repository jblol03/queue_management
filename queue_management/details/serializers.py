from rest_framework import serializers
from .models import Category, Sub_Category, Organization

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ["category"]

class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Sub_Category
        fields= ["sub_category", "category"]
        
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Organization
        fields= ["organization", "sub_category", "user"]