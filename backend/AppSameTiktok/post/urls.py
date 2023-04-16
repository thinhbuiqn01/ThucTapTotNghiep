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
    path('post_list/', views.post_list,name="post_list"),
    path('post_add/', views.post_add,name="post_add"),
    path('post_update/', views.post_update, name="post_update"),
    path('post_update_title/', views.post_update_title, name="post_update_title"),
    path('post_delete/', views.post_delete, name="post_delete")
]
