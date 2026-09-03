from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import creatgetapi,updatedeletegetidapi


urlpatterns = [
    path('register/get/',creatgetapi.as_view()),
    path('updategetdelete/<int:pk>/',updatedeletegetidapi.as_view()),
    path('token/login/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
]