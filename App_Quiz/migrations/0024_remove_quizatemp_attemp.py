# Generated by Django 3.2.5 on 2021-07-22 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Quiz', '0023_quizatemp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizatemp',
            name='attemp',
        ),
    ]
