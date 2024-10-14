from rest_framework import serializers
from ..models.models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
