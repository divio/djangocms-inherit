# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.utils.i18n import get_language_tuple
from cms.models import CMSPlugin
from cms.models.fields import PageField


class InheritPagePlaceholder(CMSPlugin):
    """
    Provides the ability to inherit plugins for a certain placeholder from an
    associated "parent" page instance
    """
    from_page = PageField(
        null=True, blank=True,
        help_text=_("Choose a page to include its plugins into this "
                    "placeholder, empty will choose current page"))

    from_language = models.CharField(
        _("language"), max_length=5, choices=get_language_tuple(), blank=True,
        null=True, help_text=_("Optional: the language of the plugins "
                               "you want"))

    # TODO: Remove this once < 3.3.1 support is dropped
    cmsplugin_ptr = models.OneToOneField(
        to=CMSPlugin,
        parent_link=True,
        related_name='djangocms_inherit_inheritpageplaceholder',
        on_delete=models.CASCADE,
    )

    def copy_relations(self, oldinstance):
        if oldinstance.from_page_id:
            self.from_page_id = oldinstance.from_page_id
