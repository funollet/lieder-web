from django.db import models
from django.utils.translation import gettext_lazy as _
from misc import markup
from misc.mlang import CharTranslation, TextTranslation, CHOICES
from misc import mlang


class LinkCategory (models.Model):

    default_catname = models.CharField (_('name'), maxlength=200, )

    def catname(self):
        from misc import mlang
        return mlang.get_text(self, 'catname')
    catname.short_description = _('name')
    
    
    default_catdescription= models.TextField (_('description'), editable=False,)
    default_catdescription_markup = models.TextField (_('description'), 
        blank=True,
        help_text = markup.MARKUP_HELP,
        )

    def catdescription(self):
        from misc import mlang
        return mlang.get_text(self, 'catdescription')
    catdescription.short_description = _('description')
    

    pub_date = models.DateTimeField (_('publication date'), )
    slug = models.SlugField (_('permalink'),
        unique=True,
        prepopulate_from=('default_catname',),
        help_text = _('Name to be linked'),
        )


    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('link categories')
        ordering = ['pub_date']
    class Admin:
        fields = (
            (None, {'fields': ('default_catname', 'default_catdescription_markup', 'pub_date',),}),
            (_('Advanced'), {'fields': ('slug',), 'classes': 'collapse',} ),
        )
        list_display = ('default_catname', 'pub_date',)

    
    def __str__ (self):
        return self.default_catname

    def save (self):
        from misc import markup
        markup.parse_markup (self)
        super(LinkCategory, self).save()

    def get_absolute_url (self):
        pass
    
    

class CatName (CharTranslation):
    parent = models.ForeignKey(LinkCategory, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for name')
        verbose_name_plural = _('translations for names')

class CatDescription (TextTranslation):
    parent = models.ForeignKey(LinkCategory, edit_inline=models.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class Meta:
        verbose_name = _('translation for description')
        verbose_name_plural = _('translations for descriptions')





class Link (models.Model):

    default_name = models.CharField (_('name'), maxlength=200, )

    def name(self):
        from misc import mlang
        return mlang.get_text(self, 'name')
    name.short_description = _('name')

    default_description = models.TextField (_('description'), editable=False,)
    default_description_markup = models.TextField (_('description'), 
        blank=True,
        help_text = markup.MARKUP_HELP,
        )

    def description(self):
        from misc import mlang
        return mlang.get_text(self, 'description')
    description.short_description = _('description')
 
    category = models.ForeignKey ( LinkCategory,
        verbose_name=_('category'),
        blank = True,
        )

    url = models.URLField (_('url'), verify_exists=False)
    pub_date = models.DateTimeField (_('publication date'), )
    slug = models.SlugField (_('permalink'),
        prepopulate_from = ('default_name',),
        unique = True,
        )


    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        ordering = ['pub_date']
    class Admin:
        list_display = ('default_name', 'category', 'url',)
        list_filter = ('category',)
        search_fields = ('default_name',)
        fields = (
            (None, {'fields': ('url',)}),
            (None, {'fields': (('default_name','category',), 'default_description_markup',
                               'pub_date',),}),
            (_('Advanced'), {'fields': ('slug',),
                    'classes': 'collapse',}),
        )


    def __str__ (self):
        return self.default_name

    def save (self):
        from misc import markup
        markup.parse_markup (self)
        super(Link, self).save()

    def get_absolute_url (self):
        pass

class Name (CharTranslation):
    parent = models.ForeignKey(Link, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

class Description (TextTranslation):
    parent = models.ForeignKey(Link, edit_inline=models.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class Meta:
        verbose_name = _('translation for Description')
        verbose_name_plural = _('translations for Descriptions')
