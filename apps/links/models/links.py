from django.core import meta
from django.utils.translation import gettext_lazy as _
from lieder.apps.misc import misc
from lieder.apps.misc.mlang import CharTranslation, TextTranslation, CHOICES
from lieder.apps.misc import mlang


class LinkCategory (meta.Model):

    default_catname = meta.CharField (_('name'), maxlength=200, )

    def catname(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'name')
    catname.short_description = _('name')
    
    
    default_catdescription= meta.TextField (_('description'), editable=False,)
    default_catdescription_markup = meta.TextField (_('description'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def catdescription(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'description')
    catdescription.short_description = _('description')
    

    pub_date = meta.DateTimeField (_('publication date'), )
    slug = meta.SlugField (_('slug'),
        unique=True,
        prepopulate_from=('default_catname',),
        help_text = _('Readable link name'),
        )


    class META:
        verbose_name = _('category')
        verbose_name_plural = _('link categories')
        ordering = ['pub_date']
        admin = meta.Admin(
            fields = (
            (None, {'fields': ('default_catname', 'default_catdescription_markup', 'pub_date',),}),
            (_('Advanced'), {'fields': ('slug',), 'classes': 'collapse',} ),
            ),
            list_display = ('default_catname', 'pub_date',),
            )

    
    def __repr__ (self):
        return self.default_catname

    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup (self)

class CatName (CharTranslation):
    parent = meta.ForeignKey(LinkCategory, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for name')
        verbose_name_plural = _('translations for names')

class CatDescription (TextTranslation):
    parent = meta.ForeignKey(LinkCategory, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for description')
        verbose_name_plural = _('translations for descriptions')





class Link (meta.Model):

    default_name = meta.CharField (_('name'), maxlength=200, )

    def name(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'name')
    name.short_description = _('name')

    default_description = meta.TextField (_('description'), editable=False,)
    default_description_markup = meta.TextField (_('description'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def description(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'description')
    description.short_description = _('description')
 
    category = meta.ForeignKey ( LinkCategory,
        verbose_name=_('category'),
        blank = True,
        )

    url = meta.URLField (_('url'), verify_exists=False)
    pub_date = meta.DateTimeField (_('publication date'), )
    slug = meta.SlugField (_('slug'),
        prepopulate_from = ('default_name',),
        unique = True,
        )


    class META:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        ordering = ['pub_date']
        admin = meta.Admin (
            list_display = ('default_name', 'category', 'url',),
            list_filter = ('category',),
            search_fields = ('default_name',),
            fields = (
            (None, {'fields': ('url',)}),
            (None, {'fields': (('default_name','category',), 'default_description_markup',
                               'pub_date',),}),
            (_('Advanced'), {'fields': ('slug',),
                    'classes': 'collapse',}),
            ),
            )


    def __repr__ (self):
        return self.default_name

    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup (self)


class Name (CharTranslation):
    parent = meta.ForeignKey(Link, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

class Description (TextTranslation):
    parent = meta.ForeignKey(Link, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for Description')
        verbose_name_plural = _('translations for Descriptions')
