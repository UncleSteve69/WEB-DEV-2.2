from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, gender, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an username")
        if not date_of_birth:
            raise ValueError("Users must have a birth date")
        if not gender:
            raise ValueError("Users must have a gender")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, gender, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_of_birth = models.DateField(verbose_name='birth date')
    gender = models.CharField(max_length=32)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'date_of_birth', 'gender']
    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


"""
class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.user, self.dark_mode)
"""