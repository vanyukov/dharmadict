# Generated by Django 3.0.8 on 2021-04-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210411_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
