# Generated by Django 4.2 on 2023-07-19 16:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pictures', '0006_favorite'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'picture')},
        ),
    ]
