from django.urls import path
from .views import (
    ApplicationCreateAPIView,
    MyApplicationsAPIView,
    EmployerApplicationsAPIView,
    ApplicationStatusUpdateAPIView
)


urlpatterns = [
    path('creatapplications/',ApplicationCreateAPIView.as_view()),
    path('myapplications/',MyApplicationsAPIView.as_view()),
    path('employerapplication/',EmployerApplicationsAPIView.as_view()),
    path('statusapplication/<int:pk>',ApplicationStatusUpdateAPIView.as_view()),
]