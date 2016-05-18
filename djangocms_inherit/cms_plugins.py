import copy

from django.conf import settings
from django.core.exceptions import FieldError
try:
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    # Django <= 1.6 compatibility
    from django.contrib.sites.models import get_current_site
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils import get_language_from_request
from cms.utils.moderator import get_cmsplugin_queryset
from cms.utils.plugins import downcast_plugins, build_plugin_tree

from .forms import InheritForm
from .models import InheritPagePlaceholder


class InheritPagePlaceholderPlugin(CMSPluginBase):
    """
    Locates the plugins associated with the "from_page" of an
    InheritPagePlaceholder instance and renders those plugins sequentially
    """
    model = InheritPagePlaceholder
    name = _("Inherit Plugins from Page")
    render_template = "cms/plugins/inherit_plugins.html"
    form = InheritForm
    admin_preview = False
    page_only = True

    def render(self, context, instance, placeholder):
        template_vars = {
            'object': instance,
            'placeholder': placeholder,
        }
        lang = instance.from_language
        request = context.get('request', None)
        if not lang:
            if 'request' in context:
                lang = get_language_from_request(request)
            else:
                lang = settings.LANGUAGE_CODE
        page = instance.placeholder.page
        from_page = instance.from_page

        if page.publisher_is_draft:
            from_page = from_page.get_draft_object()
        else:
            from_page = from_page.get_public_object()

        plugins = get_cmsplugin_queryset(request).filter(
            placeholder__page=from_page,
            language=lang,
            placeholder__slot__iexact=placeholder,
            parent__isnull=True
        ).order_by('position').select_related()

        plugin_output = []
        template_vars['parent_plugins'] = plugins

        for plg in plugins:
            tmpctx = copy.copy(context)
            tmpctx.update(template_vars)
            inst, name = plg.get_plugin_instance()
            if inst is None:
                continue
            # Get child plugins for this plugin instance, if any child plugins
            # exist
            try:
                # django CMS 3-
                plugins = [inst] + list(inst.get_descendants(include_self=True)
                                        .order_by('placeholder', 'tree_id',
                                                  'level', 'position'))
            except (FieldError, TypeError):
                # django CMS 3.1+
                plugins = [inst] + list(inst.get_descendants().order_by('path'))
            plugin_tree = downcast_plugins(plugins)
            plugin_tree[0].parent_id = None
            plugin_tree = build_plugin_tree(plugin_tree)
            #  Replace plugin instance with plugin instance with correct
            #  child_plugin_instances set
            inst = plugin_tree[0]
            outstr = inst.render_plugin(tmpctx, placeholder)
            plugin_output.append(outstr)
        template_vars['parent_output'] = plugin_output
        context.update(template_vars)
        return context

    def get_form(self, request, obj=None, **kwargs):
        if obj and obj.page:
            site = obj.page.site
        else:
            site = get_current_site(request)

        FormClass = super(InheritPagePlaceholderPlugin, self).get_form(
            request, obj, **kwargs)

        # Set the available pages to match the current site.
        FormClass.for_site(site)
        return FormClass

plugin_pool.register_plugin(InheritPagePlaceholderPlugin)
