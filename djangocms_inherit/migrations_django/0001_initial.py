# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InheritPagePlaceholder',
            fields=[
                ('from_language', models.CharField(choices=[(b'en', b'English'), (b'de', b'German'), (b'fr', b'French'), (b'pt-br', b'Brazilian Portuguese'), (b'es-mx', 'Espa\xf1ol')], max_length=5, blank=True, help_text='Optional: the language of the plugins you want', null=True, verbose_name='language')),
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('from_page', models.ForeignKey(blank=True, to='cms.Page', help_text='Choose a page to include its plugins into this placeholder, empty will choose current page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
