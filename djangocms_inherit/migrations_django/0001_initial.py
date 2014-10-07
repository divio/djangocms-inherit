# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from cms.utils.i18n import get_language_tuple

class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InheritPagePlaceholder',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('from_language', models.CharField(help_text='Optional: the language of the plugins you want', blank=True, max_length=5, choices=get_language_tuple(), verbose_name='language', null=True)),
                ('from_page', models.ForeignKey(help_text='Choose a page to include its plugins into this placeholder, empty will choose current page', blank=True, to='cms.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
