from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics

from .models import Car, Owner
from .serializers import CarSerializer, OwnerSerializer

class CarAPIView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        else:
            try:
                cars = Car.objects.get(pk=pk)
                serializer = CarSerializer(cars, many=False)
                return Response(serializer.data)
            except Exception as e:
                return Response({"messages": "Bunday moshina yoq"}, status=status.HTTP_400_BAD_REQUEST)

class OwnerAPIView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            owners = Owner.objects.all()
            serializer = OwnerSerializer(owners, many=True)
            return Response(serializer.data)
        else:
            try:
                owner = Owner.objects.get(pk=pk)
                serializer = OwnerSerializer(owner, many=False)
                return Response(serializer.data)
            except Exception as e:
                return Response({"messages": "Owner not found"}, status=status.HTTP_400_BAD_REQUEST)

class CreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class OwnerCreateAPIView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer