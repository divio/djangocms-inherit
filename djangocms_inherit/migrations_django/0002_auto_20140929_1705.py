# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_inherit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inheritpageplaceholder',
            name='from_language',
            field=models.CharField(choices=[(b'en', b'en')], max_length=5, blank=True, help_text='Optional: the language of the plugins you want', null=True, verbose_name='language'),
        ),
    ]
