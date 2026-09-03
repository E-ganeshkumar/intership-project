from django.urls import path

from .views import JobListCreateAPIView,JobDetailAPIView


urlpatterns = [
    path('jobscreate',JobListCreateAPIView.as_view()),
    path('jobs/<int:pk>/',JobDetailAPIView.as_view()),
]