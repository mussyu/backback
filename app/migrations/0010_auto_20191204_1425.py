# Generated by Django 3.0 on 2019-12-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191120_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='link',
            field=models.TextField(max_length=600, verbose_name='URL'),
        ),
    ]
