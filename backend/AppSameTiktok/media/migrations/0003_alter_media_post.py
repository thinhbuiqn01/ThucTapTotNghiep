# Generated by Django 4.1.7 on 2023-04-03 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('media', '0002_alter_media_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='post.post'),
        ),
    ]
