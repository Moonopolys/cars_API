from django.urls import path
from .views import CarDetailAPIView, CarAPIView, OwnerDetailAPIView, OwnerAPIView

urlpatterns = [
    path('cars/', CarAPIView.as_view()),
    path('cars/<int:pk>/', CarDetailAPIView.as_view()),
    path('owners/', OwnerAPIView.as_view()),
    path('owners/<int:pk>/', OwnerDetailAPIView.as_view()),
]