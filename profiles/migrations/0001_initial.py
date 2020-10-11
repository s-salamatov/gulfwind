# Generated by Django 3.1.2 on 2020-10-10 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='имя')),
                ('middle_name', models.CharField(blank=True, max_length=150, verbose_name='отчество')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='фамилия')),
                ('bio', models.TextField(blank=True, verbose_name='О себе')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/avatars', verbose_name='Фото профиля')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-updated'],
                'abstract': False,
            },
        ),
    ]
