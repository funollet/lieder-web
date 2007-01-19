from django.db import models
from django.utils.translation import gettext_lazy as _
from misc import misc
from misc.mlang import CharTranslation, TextTranslation, CHOICES
from misc import mlang


class Menu (models.Model):
    name = models.CharField (_('name'), maxlength=200, )
    pub_date = models.DateTimeField (_('publication date'), )

    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menus')
        ordering = ['pub_date']
    class Admin:
        fields = (
            (None, {'fields': ('name', 'pub_date',)}),
            )

    def __str__ (self):
        return self.name


class MenuItem (models.Model):
    default_name = models.CharField (_('name'), maxlength=200, )

    def name(self):
        from misc import mlang
        return mlang.get_text(self, 'name')
    name.short_description = _('name')
    
    url = models.URLField (_('url'), verify_exists=False, )
    # Hidden field that stores a relative link.
    relative_url = models.CharField (_('local url'), maxlength=200, blank=True, editable=False )
    menu = models.ForeignKey ( Menu, verbose_name=_('menu'), )
    pub_date = models.DateTimeField (_('publication date'), )

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
        
        from django.contrib.sites.models import Site

        self.relative_url = ''
        domain = Site.objects.all()[0].domain
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
    parent = models.ForeignKey(MenuItem, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

