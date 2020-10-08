import uuid

from django.contrib.auth import password_validation
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.contrib.sites.shortcuts import get_current_site
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


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    secret_hash = models.UUIDField('хэш', default=uuid.uuid4, editable=False)

    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True,
        help_text='Ваш аккаунт будет доступен по ссылке gulfwind.ru/account/<username>'
    )
    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField('последний вход', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    class Meta:
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @classmethod
    def active_users(cls, method=None, **kwargs):
        queryset = cls.objects.filter(is_active=True, **kwargs)
        if method == 'get':
            queryset = queryset.get()
        return queryset
