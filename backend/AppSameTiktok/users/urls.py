from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .serializer import UserSerializer
from .views import UserViewset, login_user, register_user, update_name
from . import views
from rest_framework.authtoken.views import obtain_auth_token


# from .views import index
router = DefaultRouter()
router.register('users', UserViewset, basename="users")


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('login/',login_user,name ='login'),  
    # path('logout/',login.Logout,name ='logout'),  
    path('register/',register_user,name ='register'),  
    path('update_name/',views.update_name,name ='update_name'),  
    path('update_phone/',views.update_phone,name ='update_phone'), 
    path('update_email/',views.update_email,name ='update_email'), 
    # path('block/<int:id>/', api.block_user , name="block_user"),
    # path('unblock/<int:id>/', api.unblock_user , name="unblock_user"),

    
]