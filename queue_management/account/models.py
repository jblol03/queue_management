from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.crypto import get_random_string

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
   
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, name, and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class EndUserManager(BaseUserManager):
    def create_enduser(self, email, name, otp=None):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            otp=otp
        )
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# Custom End User Model

class EndUserManager(BaseUserManager):
    def create_enduser(self, email, name):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.generate_otp()  # Generate OTP on user creation
        user.save(using=self._db)
        return user

class EndUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_enduser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = EndUserManager()

    def __str__(self):
        return self.email

    def generate_otp(self):
        self.otp = get_random_string(length=6, allowed_chars='0123456789')