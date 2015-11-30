=================
djangocms-inherit
=================

An inherit plugin for django CMS. This plugin will render the plugins from a
specified page (and language) in its place.


------------
Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

1. In your projects `virtualenv`, run ``pip install djangocms-inherit``.
2. Add ``'djangocms_inherit'`` to your ``INSTALLED_APPS`` setting.
3. If using Django 1.6 add ``'djangocms_inherit': 'djangocms_inherit.south_migrations',``
   to ``SOUTH_MIGRATION_MODULES``  (define ``SOUTH_MIGRATION_MODULES`` if it
   does not already exist).
4. Run ``manage.py migrate djangocms_inherit``.


------------
Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-inherit/
