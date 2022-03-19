from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountMenager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Użytkownik musi posiadać nazwe użytkownika")
        
        user = self.model(username=username,)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password,)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

        



class Account(AbstractBaseUser):
    #Informacje o koncie
    username            = models.CharField(verbose_name="username", max_length=32, unique=True)
    discord_id          = models.CharField(verbose_name="discord_id", max_length=32, unique=False, blank=True)
    email               = models.EmailField(verbose_name="email", max_length=100, unique=False, blank=True)
    
    #Waluty
    cny                 = models.IntegerField(verbose_name="Yuan", default=0)
    rub                 = models.IntegerField(verbose_name="Rubel", default=0)
    lir                 = models.IntegerField(verbose_name="Lira", default=0)
    clp                 = models.IntegerField(verbose_name="Peso chilijskie", default=0)
    tp                  = models.IntegerField(verbose_name="Peso tarpijskie", default=0)
    
    #Inne wymagane
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    is_organization     = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['']

    objects = MyAccountMenager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True