from django.db import models
from django.utils.translation import gettext_lazy as _
from misc import misc
from misc.mlang import CharTranslation, TextTranslation, CHOICES
from misc import mlang

STATUS_CHOICES = (
    ('drf', _('draft')),
    ('rvs', _('revision')),
    ('pbl', _('public')),
    ('rch', _('archived')),
    ('ntr', _('internal')),
    )


class Section (models.Model):
    default_secname = models.CharField (_('name'), maxlength=200, )

    def secname(self):
        from misc import mlang
        return mlang.get_text(self, 'secname')
    secname.short_description = _('name')
    
    slug = models.SlugField (_('permalink'),
        prepopulate_from = ('default_secname',),
        unique = True,
        help_text = _('Name to be linked'),
    )
    pub_date = models.DateTimeField (_('publication date'), )

        
    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
    class Admin:
        pass
    
    def __str__ (self):
        return self.default_secname
    
    def get_absolute_url (self):
        pass

    def show_image (self):
        if self.slug == 'la-direccio':
            return True
        else:
            return False
    
    def show_intro (self):
        if self.slug in ['la-direccio', 'la-premsa-ha-dit']:
            return True
        else:
            return False


class SecName (CharTranslation):
    parent = models.ForeignKey(Section, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')


    
class PublicStatusManager (models.Manager):
    def get_query_set (self):
        return super(PublicStatusManager, self).get_query_set().filter(status='pbl')
    


class Article (models.Model):
    
    status = models.CharField (_('status'), maxlength=3, 
        choices=STATUS_CHOICES,
        default='drf',
        radio_admin=True,
        )
    section = models.ForeignKey (Section,
        verbose_name=_('section'),)
 
    default_name = models.CharField (_('name'), maxlength=200, )

    def name(self):
        from misc import mlang
        return mlang.get_text(self, 'name')
    name.short_description = _('name')
    
    default_intro= models.TextField (_('introduction'), editable=False,)
    default_intro_markup = models.TextField (_('introduction'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def intro(self):
        from misc import mlang
        return mlang.get_text(self, 'intro')
    intro.short_description = _('intro')

    default_body= models.TextField (_('body'), editable=False,)
    default_body_markup = models.TextField (_('body'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def body(self):
        from misc import mlang
        return mlang.get_text(self, 'body')
    body.short_description = _('body')


    pub_date = models.DateTimeField (_('publication date'))
    slug = models.SlugField (_('permalink'),
        prepopulate_from = ('default_name',),
        unique = True,
        help_text = _('Name to be linked'),
        )
    image = models.ImageField (_('image'),
        upload_to = 'articles',
        blank = True,
        )

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ['-pub_date']
    class Admin:
        list_display = ('default_name', 'section', 'pub_date',)
        list_filter = ('status', 'section',)
        search_fields = ('default_name',)
        fields = (
            (None, {
            'fields': (('default_name', 'section'), ('status',),)}
             ),
            (_('Introduction'), {
            'classes': 'collapse',
            'fields': ('default_intro_markup',),
            }),
            (_('Body'), {
            'fields': ('default_body_markup',),
            }),
            (None, {
            'fields': ('pub_date',),
            }),
            (_('Advanced'), {
            'classes': 'collapse',
            'fields': ('slug', 'image',),
            }),
        )
        

    def __str__ (self):
        return self.default_name
    
    def save (self):
        from misc import misc
        misc.parse_markup (self)
        super(Article, self).save()

    def get_absolute_url (self):
        pass

    def show_image (self):
        return True
    
    def show_title (self):
        if self.section.slug == 'programes' :
            return True
        return False

    objects = models.Manager()
    public_objects = PublicStatusManager()
    


class Name (CharTranslation):
    parent = models.ForeignKey(Article, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

class Intro (TextTranslation):
    parent = models.ForeignKey(Article, edit_inline=models.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class Meta:
        verbose_name = _('translation for introduction')
        verbose_name_plural = _('translations for introductions')
        
class Body (TextTranslation):
    parent = models.ForeignKey(Article, edit_inline=models.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class Meta:
        verbose_name = _('translation for Body')
        verbose_name_plural = _('translations for Bodys')
