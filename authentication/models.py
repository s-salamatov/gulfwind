import uuid

from django.contrib.auth import password_validation
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.core.mail import send_mail
from django.db import models

from core.models import TimestampedModel


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Пользователи должен указать короткое имя (username)')

        if email is None:
            raise TypeError('Пользователь должен указать email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
      if password is None:
          raise TypeError('Суперпользователь должен указать пароль')

      user = self.create_user(username, email, password)
      user.is_superuser = True
      user.is_staff = True
      user.save()

      return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    readable_id = models.AutoField(auto_created=True, verbose_name='readable_id', editable=False)
    secret_hash = models.UUIDField('хэш', default=uuid.uuid4, editable=False)

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)

    first_name = models.CharField('имя', max_length=150, blank=True)
    last_name = models.CharField('фамилия', max_length=150, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    last_login = models.DateTimeField('последний вход', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @classmethod
    def active_users(cls, method=None, **kwargs):
        queryset = cls.objects.filter(is_active=True, **kwargs)
        if method == 'get':
            queryset = queryset.get()
        return queryset
