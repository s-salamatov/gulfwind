import uuid

from django.db import models

from core.models import TimestampedModel


class HostelReport(TimestampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    secret_hash = models.UUIDField('хэш', default=uuid.uuid4, editable=False)

    author = models.ForeignKey('authentication.User', on_delete=models.CASCADE, verbose_name='автор')

    start_date = models.DateField('дата ухода в увольнение')
    end_date = models.DateField('дата выхода с увольнения')
    reason = models.CharField('причина ухода в увольнение', max_length=1000)
    addr = models.CharField('адрес нахождения в увольнении', max_length=1000)

    comment = models.TextField('дополнительная информация')
