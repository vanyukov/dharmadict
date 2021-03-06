# Generated by Django 3.0.8 on 2021-05-29 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20210506_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='img',
            field=models.ImageField(blank=True, default='static/user.jpg', null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_page', to='core.Page'),
        ),
    ]
