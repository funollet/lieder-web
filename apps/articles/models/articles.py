from django.core import meta
from django.utils.translation import gettext_lazy as _
from lieder.apps.misc import misc
from lieder.apps.misc.mlang import CharTranslation, TextTranslation, CHOICES
from lieder.apps.misc import mlang

STATUS_CHOICES = (
    ('drf', _('draft')),
    ('rvs', _('revision')),
    ('pbl', _('public')),
    ('rch', _('archived')),
    ('ntr', _('internal')),
    )


class Section (meta.Model):
    default_secname = meta.CharField (_('name'), maxlength=200, )

    def secname(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'secname')
    secname.short_description = _('name')
    
    slug = meta.SlugField (_('permalink'),
        prepopulate_from = ('default_secname',),
        unique = True,
        help_text = _('Name to be linked'),
    )
    pub_date = meta.DateTimeField (_('publication date'), )

        
    class META:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
        admin = meta.Admin()
        
    def __repr__ (self):
        return self.default_secname
    
    def get_absolute_url (self):
        pass



class SecName (CharTranslation):
    parent = meta.ForeignKey(Section, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')



class Article (meta.Model):
    
    status = meta.CharField (_('status'), maxlength=3, 
        choices=STATUS_CHOICES,
        default='drf',
        )
    section = meta.ForeignKey (Section,
        verbose_name=_('section'),)
 
    default_name = meta.CharField (_('name'), maxlength=200, )

    def name(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'name')
    name.short_description = _('name')
    
    default_intro= meta.TextField (_('introduction'), editable=False,)
    default_intro_markup = meta.TextField (_('introduction'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def intro(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'intro')
    intro.short_description = _('intro')

    default_body= meta.TextField (_('body'), editable=False,)
    default_body_markup = meta.TextField (_('body'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def body(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'body')
    body.short_description = _('body')


    pub_date = meta.DateTimeField (_('publication date'),
        auto_now_add = True, )
    slug = meta.SlugField (_('permalink'),
        prepopulate_from = ('default_name',),
        unique = True,
        help_text = _('Name to be linked'),
        )
    image = meta.ImageField (_('image'),
        upload_to = 'articles',
        blank = True,
        )

    
    class META:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        admin = meta.Admin (
            list_display = ('default_name', 'section', 'pub_date',),
            list_filter = ('status', 'section',),
            fields = (
            (None, {
            'fields': (('default_name', 'section', 'status'),)}
             ),
            (_('Introduction'), {
            'classes': 'collapse',
            'fields': ('default_intro_markup',),
            }),
            (None, {
            'fields': ('default_body_markup',),
            }),
            (_('Advanced'), {
            'classes': 'collapse',
            'fields': ('slug', 'image',),
            }),
            ),            
            )
        

    def __repr__ (self):
        return self.default_name
    
    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup (self)

    def get_absolute_url (self):
        pass


class Name (CharTranslation):
    parent = meta.ForeignKey(Article, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for Name')
        verbose_name_plural = _('translations for Names')

class Intro (TextTranslation):
    parent = meta.ForeignKey(Article, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for introduction')
        verbose_name_plural = _('translations for introductions')
        
class Body (TextTranslation):
    parent = meta.ForeignKey(Article, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for Body')
        verbose_name_plural = _('translations for Bodys')
