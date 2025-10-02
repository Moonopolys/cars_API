from itertools import product

from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics

from .models import Car, Owner, Brand
from .serializers import CarSerializer, OwnerSerializer, BrandSerializer

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

    def post(self, request, pk: int = None):
        if pk:
            return Response({"message": "Method POST not allowed!!!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = CarSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            cars = serializer.save()

            return Response(CarSerializer(cars).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk: int = None):
        if not pk:
            return Response({"message": f"Method {request.method} not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                cars = Car.objects.get(pk=pk)
            except Exception as a:
                return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = CarSerializer(instance=cars, data=request.data,
                                       partial=True if request.method == "PATCH" else False)
            serializer.is_valid(raise_exception=True)
            cars = serializer.save()
            return Response(CarSerializer(cars).data)

    def patch(self, request, pk: int = None):
        return self.put(request, pk)

    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"message": f"Method {request.method} not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                cars = Car.objects.get(pk=pk)
            except Exception as a:
                return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

            cars.delete()
            return Response({"message": "Car deleted successfully!!!"}, status=status.HTTP_204_NO_CONTENT)

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

    def post(self, request, pk: int = None):
        if pk:
            return Response({"message": "Method POST not allowed!!!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = OwnerSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            owner = serializer.save()

            return Response(OwnerSerializer(owner).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk: int = None):
        if not pk:
            return Response({"message": f"Method {request.method} not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                owner = Owner.objects.get(pk=pk)
            except Exception as a:
                return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = OwnerSerializer(instance=owner, data=request.data,
                                       partial=True if request.method == "PATCH" else False)
            serializer.is_valid(raise_exception=True)
            owner = serializer.save()
            return Response(OwnerSerializer(owner).data)

    def patch(self, request, pk: int = None):
        return self.put(request, pk)

    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"message": f"Method {request.method} not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                owner = Owner.objects.get(pk=pk)
            except Exception as a:
                return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

            owner.delete()
            return Response({"message": "Owner deleted successfully!!!"}, status=status.HTTP_204_NO_CONTENT)



class BrandAPIView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            brand = Brand.objects.all()
            serializer = BrandSerializer(brand, many=True)
            return Response(serializer.data)
        else:
            try:
                brand = Brand.objects.get(pk=pk)
                serializer = BrandSerializer(brand, many=False)
                return Response(serializer.data)
            except Exception as e:
                return Response({"messages": "Brand not found"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk: int = None):
        if pk:
            return Response({"message": "Method POST not allowed!!!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = BrandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            brand = serializer.save()

            return Response(BrandSerializer(brand).data, status=status.HTTP_201_CREATED)

    def put(self, request, pk: int = None):
        if not pk:
            return Response({"message": f"Method {request.method} not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                brand = Brand.objects.get(pk=pk)
            except Exception as a:
                return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = BrandSerializer(instance=brand, data=request.data,
                                       partial=True if request.method == "PATCH" else False)
            serializer.is_valid(raise_exception=True)
            brand = serializer.save()
            return Response(BrandSerializer(brand).data)

    def patch(self, request, pk: int = None):
        return self.put(request, pk)

    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({"message": f"Method {request.method} not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                brand = Brand.objects.get(pk=pk)
            except Exception as a:
                return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)

            brand.delete()
            return Response({"message": "Brand deleted successfully!!!"}, status=status.HTTP_204_NO_CONTENT)


class CreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class OwnerCreateAPIView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer