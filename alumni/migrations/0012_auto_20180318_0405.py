# Generated by Django 2.0.3 on 2018-03-17 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0011_auto_20180317_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_image',
            field=models.ImageField(default='profile_img/profile.png', upload_to='profile_img'),
        ),
        migrations.AddField(
            model_name='post',
            name='author_image',
            field=models.ImageField(default='profile_img/profile.png', upload_to='profile_img'),
        ),
    ]
