from django.db import models
from django.utils.translation import gettext_lazy as _
from lieder.apps.misc import misc
from lieder.apps.misc.mlang import CharTranslation, TextTranslation, CHOICES
from lieder.apps.misc import mlang


class Menu (models.Model):
    name = meta.CharField (_('name'), maxlength=200, )
    pub_date = meta.DateTimeField (_('publication date'), )

    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menus')
        ordering = ['pub_date']
    class Admin:
        fields = (
            (None, {'fields': (('name', 'pub_date',),),}),
            ),

    def __str__ (self):
        return self.name


class MenuItem (models.Model):
#     name = meta.CharField (_('item short name'), maxlength=200, )
    default_name = meta.CharField (_('name'), maxlength=200, )

    def name(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'name')
    name.short_description = _('name')
    
    url = meta.URLField (_('url'), verify_exists=False, )
    # Hidden field that stores a relative link.
    relative_url = meta.CharField (_('local url'), maxlength=200, blank=True, editable=False )
    menu = meta.ForeignKey ( Menu, verbose_name=_('menu'), )
    pub_date = meta.DateTimeField (_('publication date'), )

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')
        ordering = ['pub_date']
    class Admin:
        list_display = ('menu', 'default_name', 'url',)
        list_filter = ('menu',)

    def __str__ (self):
        return self.default_name

    def save (self) :
        """If url is a local link, stores as a relative link. """
        
        #TODO: import sites, build domain with Manager
        from django.models.core import sites

        self.relative_url = ''
        domain = sites.get_object(pk=1).domain
        if domain in self.url :
            begin = self.url.find (domain)
            self.relative_url = self.url[begin+len(domain):]
            
        super(MenuItem, self).save()


    def get_link (self):
        """Returns url or relative_url where appropiate."""
        if self.relative_url != '':
            return self.relative_url
        else:
            return self.url


class Name (CharTranslation):
    parent = meta.ForeignKey(MenuItem, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

