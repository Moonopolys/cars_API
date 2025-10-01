from django.urls import path
from .views import CarAPIView, OwnerAPIView, CreateAPIView, OwnerCreateAPIView

urlpatterns = [
    path('cars/', CarAPIView.as_view()),
    path('cars/<int:pk>', CarAPIView.as_view()),
    path('cars/create/', CreateAPIView.as_view()),
    path('owner/', OwnerAPIView.as_view()),
    path('owner/<int:pk>', OwnerAPIView.as_view()),
    path('owner/create/', OwnerCreateAPIView.as_view()),

]