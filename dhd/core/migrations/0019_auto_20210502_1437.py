# Generated by Django 3.0.8 on 2021-05-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_meaning_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meaning',
            name='meaning',
            field=models.CharField(max_length=512),
        ),
    ]
