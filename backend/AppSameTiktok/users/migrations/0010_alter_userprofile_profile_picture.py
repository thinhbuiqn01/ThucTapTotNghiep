# Generated by Django 4.1.7 on 2023-04-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='userprofile/user.jpg', upload_to='userprofile'),
        ),
    ]
