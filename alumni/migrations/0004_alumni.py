# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-01-31 13:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni', '0003_post_approved_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('profile_img', models.ImageField(default='images/profile.png', upload_to='images/')),
                ('passout_year', models.IntegerField(blank=True, choices=[(1997, b'1997'), (1998, b'1998'), (1999, b'1999'), (2000, b'2000'), (2001, b'2001'), (2002, b'2002'), (2003, b'2003'), (2004, b'2004'), (2005, b'2005'), (2006, b'2006'), (2007, b'2007'), (2008, b'2008'), (2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015'), (2016, b'2016'), (2017, b'2017'), (2018, b'2018'), (2019, b'2019'), (2020, b'2020'), (2021, b'2021')], default=2016)),
                ('fb_link', models.URLField(null=True)),
                ('ln_link', models.URLField(null=True)),
                ('curr_work', models.CharField(blank=True, max_length=100)),
                ('prev_work', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
