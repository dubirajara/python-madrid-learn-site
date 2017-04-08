from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomBaseUserManager(BaseUserManager):
    def create_user(self, username, email, full_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, password):
        user = self.create_user(username, email,
                                full_name,
                                password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def upload_user_photo_path(instance, filename):
    return '{0}/{1}'.format(instance.username, filename)


class UserLearn(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=50, unique=True)
    email = models.EmailField('email address', unique=True)
    full_name = models.CharField('full name', max_length=100)
    bio = models.TextField('biography', null=True, blank=True)
    url = models.URLField('URL', max_length=200, null=True, blank=True)
    photo = models.ImageField('photo', upload_to=upload_user_photo_path,
                              null=True, blank=True,)
    create_at = models.DateTimeField('create at', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomBaseUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

