# Generated by Django 3.2 on 2021-07-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='tutul.jpg', upload_to='photo'),
        ),
    ]
