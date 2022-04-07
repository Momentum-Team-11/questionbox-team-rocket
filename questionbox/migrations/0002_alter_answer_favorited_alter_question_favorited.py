# Generated by Django 4.0.3 on 2022-04-07 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='answer_favorited', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='question_favorited', to=settings.AUTH_USER_MODEL),
        ),
    ]
