# Generated by Django 3.2 on 2023-10-24 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(default='image', max_length=200, unique=True),
        ),
    ]
