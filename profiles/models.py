from django.db import models

from core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)

    first_name = models.CharField('имя', max_length=150, blank=True)
    middle_name = models.CharField('отчество', max_length=150, blank=True)
    last_name = models.CharField('фамилия', max_length=150, blank=True)

    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        full_name = '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        short_name = '%s %s' % (self.first_name, self.middle_name)
        return short_name.strip()
