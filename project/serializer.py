from rest_framework import serializers
from .models import histoy

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = histoy
        fields = ['history']