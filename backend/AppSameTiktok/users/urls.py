from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .serializer import UserSerializer
from .views import UserViewset,ProfileViewset, login_user, register_user, update_name
from . import views
from rest_framework.authtoken.views import obtain_auth_token


# from .views import index
router = DefaultRouter()
router.register('users', UserViewset, basename="users")
router.register('profile',ProfileViewset, basename="profile")


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('login/',login_user,name ='login'),  
    path('update_full_address/',views.update_full_address,name ='update_full_address'),  
    path('register/',register_user,name ='register'),  
    path('update_name/',views.update_name,name ='update_name'),  
    path('update_phone/',views.update_phone,name ='update_phone'), 
    path('update_email/',views.update_email,name ='update_email'), 
    path('update_profile_picture/', views.update_profile_picture , name="update_profile_picture"),
    # path('unblock/<int:id>/', api.unblock_user , name="unblock_user"),

    
]