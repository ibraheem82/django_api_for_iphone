from django.db import models
# from enum import unique
# ! [AbstractUser] for creating django custom user model
from django.contrib.auth.models import AbstractUser
# ! [BaseUserManager] will dictate how we are going to create our [superusers] as well as our [normal users of our application] manager.
# ! the [manager] will dictate how our user objects will be created.
from django.contrib.auth.base_user import BaseUserManager


# ===> [ ugettext_lazy ] it helps us to throw a value error when the email is not provided
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
#===#

# ! Don't forget to put [ AUTH_USER_MODEL = 'authentication.User' ] in your settings.py file
#  *
#  *
#  *
#  */





# ===> we want to overwrite the [ create user ] method and the [ create superuser ] method
# ===> ===>    <===
class CustomerUserManager(BaseUserManager):
    # ===> the requires fields 
    # [ **extra_fields ] are associated with the user model
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))
        # [ normalize_email ] takes in the email that you have provided and count the domain path of an email into lowercase
        email = self.normalize_email(email)
            # [ ] for our new_user
        new_user = self.model(email=email, **extra_fields)
        
        # [ set_password ] get password for the new user and then hash the password before storing it
        new_user.set_password(password)
        
        new_user.save()
        
        return new_user
        
    
    def create_user(self, email, password, **extra_fields):
        # [] our superuser is a staff user
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        
        # ===> if any of the fields provided is a false then raise a [ ValueError ]
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))


        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))
        
        return self.create_user(email, password, **extra_fields)
    
    
    
    
class User(AbstractUser):
    username = models.CharField(max_length = 40, unique = True)
    email = models.EmailField(max_length = 80, unique = True)
    phone_number = PhoneNumberField(null = False, unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']
    
    
    # create user using custom user manager
    objects = CustomerUserManager()
    
    
    def __str__(self):
        return f"<user {self.email} "


