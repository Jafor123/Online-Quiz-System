# Generated by Django 3.2 on 2021-07-18 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Quiz', '0021_tournamentquestion_attemp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoty',
            name='attemp1',
        ),
        migrations.RemoveField(
            model_name='categoty',
            name='attemp1_s',
        ),
        migrations.RemoveField(
            model_name='categoty',
            name='attemp2',
        ),
        migrations.RemoveField(
            model_name='categoty',
            name='attemp2_s',
        ),
        migrations.RemoveField(
            model_name='categoty',
            name='attemp3',
        ),
        migrations.RemoveField(
            model_name='categoty',
            name='attemp3_s',
        ),
    ]