# Generated by Django 2.0 on 2018-03-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0014_auto_20180322_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='n/a', upload_to='images/uploads'),
            preserve_default=False,
        ),
    ]