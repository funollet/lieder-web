from django.core import meta
from django.utils.translation import gettext_lazy as _
from lieder.apps.misc import misc
from lieder.apps.misc.mlang import CharTranslation, TextTranslation, CHOICES
from lieder.apps.misc import mlang

class DocumentCategory (meta.Model):
#     name = meta.CharField (_('name'),
#         maxlength=200,
#         )
#     description = meta.TextField (_('description'), editable=False,)
#     description_markup = meta.TextField (_('description'), 
#         blank=True,
#         help_text = misc.MARKUP_HELP,
#         )

    default_catname = meta.CharField (_('name'), maxlength=200, )

    def catname(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'catname')
    catname.short_description = _('name')
    
    default_catdescription= meta.TextField (_('description'), editable=False,)
    default_catdescription_markup = meta.TextField (_('description'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def catdescription(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'catdescription')
    catdescription.short_description = _('description')

    pub_date = meta.DateTimeField (_('publication date'), )
    slug = meta.SlugField (_('slug'),
        unique=True,
        prepopulate_from=('default_catname',),
        help_text = _('Readable link name'),
        )

    class META:
        verbose_name = _('category')
        verbose_name_plural = _('document categories')
        ordering = ['pub_date']
        admin = meta.Admin(
            fields = (
            (None, {'fields': ('default_catname', 'default_catdescription_markup', 'pub_date',),}),
            (_('Advanced'), {'fields': ('slug',), 'classes': 'collapse',}),
            ),
            )


    def __repr__ (self):
        return self.default_catname

    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup (self)


class CatName (CharTranslation):
    parent = meta.ForeignKey(DocumentCategory, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
       
    class META:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

class CatDescription (TextTranslation):
    parent = meta.ForeignKey(DocumentCategory, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
       
    class META:
        verbose_name = _('translation for Description')
        verbose_name_plural = _('translations for Descriptions')





class Document (meta.Model):
#     name = meta.CharField (_('document short name'), maxlength=200,
#         )
#     description = meta.TextField (_('description'), editable=False,)
#     description_markup = meta.TextField (_('description'), 
#         help_text = misc.MARKUP_HELP, blank=True, )
    
    default_name = meta.CharField (_('name'), maxlength=200, )

    def name(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'name')
    name.short_description = _('name')
    
    default_description= meta.TextField (_('description'), editable=False,)
    default_description_markup = meta.TextField (_('description'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def description(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'description')
    description.short_description = _('description')

    category = meta.ForeignKey ( DocumentCategory,
        verbose_name=_('category'),
        blank = True,
        )

    file = meta.FileField (_('document'), upload_to='documents',
        blank = True,
        )
    pub_date = meta.DateTimeField (_('publication date'), )
    slug = meta.SlugField (_('slug'),
        prepopulate_from = ('default_name',),
        unique = True,
        )


    class META:
        verbose_name = _('document')
        verbose_name_plural = _('documents')
        ordering = ['pub_date']
        admin = meta.Admin (
            list_display = ('default_name', 'category',),
            list_filter = ('category',),
            search_fields = ('default_name',),
            fields = (
            (None, {'fields': ('file',)}),
            (None, {'fields': (('default_name','category',), 'default_description_markup',
                               'pub_date',),}),
            (_('Advanced'), {'fields': ('slug',), 'classes': 'collapse',}),
            ),
            )


    def __repr__ (self):
        return self.default_name
    
    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup (self)

class Name (CharTranslation):
    parent = meta.ForeignKey(Document, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

class Description (TextTranslation):
    parent = meta.ForeignKey(Document, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for Description')
        verbose_name_plural = _('translations for Descriptions')
