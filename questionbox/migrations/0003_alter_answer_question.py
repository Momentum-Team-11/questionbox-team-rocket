# Generated by Django 4.0.3 on 2022-04-12 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionbox', '0002_alter_answer_favorited_alter_question_favorited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questionbox.question'),
        ),
    ]
