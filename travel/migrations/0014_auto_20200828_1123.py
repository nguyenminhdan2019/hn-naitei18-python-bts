# Generated by Django 3.1 on 2020-08-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_merge_20200827_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='images/tours/5'),
        ),
    ]
