# Generated by Django 5.0.6 on 2024-06-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_profile', '0002_remove_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]
