# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0039_remove_contest_is_external'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='math_engine',
            field=models.CharField(choices=[(b'svg', 'SVG'), (b'png', 'PNG'), (b'tex', 'LaTeX'), (b'mml', 'MathML'), (b'tex+', 'MathJax'), (b'svg+', 'MathJax with SVG fallback')], default=b'svg+', help_text='the rendering engine used to render math', max_length=4, verbose_name='math engine'),
        ),
    ]