# Generated by Django 2.2.7 on 2019-11-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='画像'),
        ),
    ]