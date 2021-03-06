# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-10 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20170710_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='canonical',
            field=models.BooleanField(default=False, help_text='This Domain is the primary one where the documentation is served from.', verbose_name='Canonical'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='count',
            field=models.IntegerField(default=0, help_text='Number of times this domain has been hit.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='allow_promos',
            field=models.BooleanField(default=True, help_text='Allow sponsor advertisements on my project documentation', verbose_name='Sponsor advertisements'),
        ),
        migrations.AlterField(
            model_name='project',
            name='comment_moderation',
            field=models.BooleanField(default=False, verbose_name='Comment Moderation)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='requirements_file',
            field=models.CharField(blank=True, default=None, help_text='A <a href="https://pip.pypa.io/en/latest/user_guide.html#requirements-files"> pip requirements file</a> needed to build your documentation. Path from the root of your project.', max_length=255, null=True, verbose_name='Requirements file'),
        ),
    ]
