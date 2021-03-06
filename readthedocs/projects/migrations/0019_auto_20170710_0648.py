# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-10 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_fix-translation-model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='canonical',
            field=models.BooleanField(default=False, help_text='This Domain is the primary one where the documentation is served from'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='count',
            field=models.IntegerField(default=0, help_text='Number of times this domain has been hit'),
        ),
        migrations.AlterField(
            model_name='project',
            name='allow_promos',
            field=models.BooleanField(default=True, help_text='If unchecked, users will still see community ads.', verbose_name='Allow paid advertising'),
        ),
        migrations.AlterField(
            model_name='project',
            name='comment_moderation',
            field=models.BooleanField(default=False, verbose_name='Comment Moderation'),
        ),
        migrations.AlterField(
            model_name='project',
            name='conf_py_file',
            field=models.CharField(blank=True, default=b'', help_text='Path from project root to <code>conf.py</code> file (ex. <code>docs/conf.py</code>). Leave blank if you want us to find it for you.', max_length=255, verbose_name='Python configuration file'),
        ),
        migrations.AlterField(
            model_name='project',
            name='has_valid_webhook',
            field=models.BooleanField(default=False, help_text='This project has been built with a webhook'),
        ),
        migrations.AlterField(
            model_name='project',
            name='programming_language',
            field=models.CharField(blank=True, choices=[(b'words', b'Only Words'), (b'py', b'Python'), (b'js', b'JavaScript'), (b'php', b'PHP'), (b'ruby', b'Ruby'), (b'perl', b'Perl'), (b'java', b'Java'), (b'go', b'Go'), (b'julia', b'Julia'), (b'c', b'C'), (b'csharp', b'C#'), (b'cpp', b'C++'), (b'objc', b'Objective-C'), (b'other', b'Other')], default=b'words', help_text='The primary programming language the project is written in.', max_length=20, verbose_name='Programming Language'),
        ),
    ]
