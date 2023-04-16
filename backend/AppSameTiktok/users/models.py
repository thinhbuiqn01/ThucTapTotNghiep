from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, first_name=None, last_name = None,):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            )
        
        user.set_password(password)
        user.role_user = 3
        user.is_active = True
        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email= self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.role_user = 1
        user.save(using =self._db)
        return user
        
class Users(AbstractBaseUser):
    username        = models.CharField(max_length=50, unique = True)
    first_name      = models.CharField(max_length = 50,blank=True,null=True)
    last_name       = models.CharField(max_length = 50,blank=True,null=True)
    email           = models.EmailField(max_length = 50, unique = True)
    phone_number    = models.CharField(max_length = 10, blank=True,null=True, unique=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    role_user       = models.IntegerField(default=3)
    is_staff        = models.BooleanField(default = False)
    is_active       = models.BooleanField(default = False)
    is_superadmin   = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    remember_token  = models.CharField(max_length=255, blank=True, null=True)
    
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    date_joined     = models.DateTimeField(auto_now_add = True)
    last_login      = models.DateTimeField(auto_now_add = True)
    
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = MyAccountManager()
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
class UserProfile(models.Model):
    user = models.ForeignKey(Users, related_name="profile", on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile', default='userprofile/user.jpg')
    sex = models.IntegerField(blank=True, default=None, null=True)
    day_of_birth = models.DateField(blank=True, default=None, null= True)
    country = models.CharField(max_length=50 ,blank =True, null=True)
    city = models.CharField(max_length=50 ,blank =True, null=True)
    district = models.CharField(max_length=50 ,blank =True, null=True)
    state = models.CharField(max_length=50 ,blank =True, null=True)
    address = models.CharField(blank=True, max_length = 100, null=True)

    def __str__(self):
        return self.user.username
    
    @property
    def full_address(self):
        return "{0}, {1}, {2}, {3}, {4}".format(self.address, self.state, self.district, self.city, self.country)
    
    
    
    
        
    
    
    