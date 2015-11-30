# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_inherit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inheritpageplaceholder',
            name='from_page',
            field=cms.models.fields.PageField(null=True, to='cms.Page', help_text='Choose a page to include its plugins into this placeholder, empty will choose current page', blank=True),
            preserve_default=True,
        ),
    ]
