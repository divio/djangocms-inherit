# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_inherit', '0002_auto_20150622_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inheritpageplaceholder',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='djangocms_inherit_inheritpageplaceholder', primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE),
        ),
    ]
