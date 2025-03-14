from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .serializer import HistorySerializer
from .models import histoy


# Create your views here.
class CalculatorAPIView(APIView):

    def post(self, request):
        history = request.data.get("history")
        expersion = histoy.objects.create(history=history)
        return Response({"message": "successful"}, status=status.HTTP_200_OK)

    def get(self, request):
        historys = histoy.objects.all().order_by('-created_at')
        serializer = HistorySerializer(historys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
