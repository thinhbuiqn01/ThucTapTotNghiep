from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .serializer import PostSerializer
from .views import Postviewset
from . import views
from rest_framework.authtoken.views import obtain_auth_token


# from .views import index
router = DefaultRouter()
router.register('post', Postviewset, basename="postviewset")

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('allpost/', views.allpost,name="allpost"),

]