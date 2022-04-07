# Generated by Django 4.0.3 on 2022-04-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
