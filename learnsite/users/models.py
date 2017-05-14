from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomBaseUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(username, email,
                                password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def upload_user_photo_path(instance, filename):
    return '{0}/{1}'.format(instance.username, filename)


class UserLearn(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=50, unique=True,
                                error_messages={'unique': "This username has already been registered."})
    email = models.EmailField('email address', unique=True)
    full_name = models.CharField('full name', max_length=100, null=True, blank=True)
    bio = models.TextField('biography', null=True, blank=True)
    url = models.URLField('URL', max_length=200, null=True, blank=True)
    photo = models.ImageField('photo', upload_to=upload_user_photo_path,
                              null=True, blank=True, )
    joined = models.DateTimeField('joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomBaseUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username
