# Generated by Django 2.0 on 2018-03-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_pet_is_castrated'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]