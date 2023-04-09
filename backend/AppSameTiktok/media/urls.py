from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Mediaviewset
from . import views
from rest_framework.authtoken.views import obtain_auth_token


# from .views import index
router = DefaultRouter()
router.register('', Mediaviewset, basename="mediaviewset")

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),

]