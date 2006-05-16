from django.core import meta
from django.utils.translation import gettext_lazy as _
from lieder.apps.misc import misc
from lieder.apps.misc.mlang import CharTranslation, TextTranslation, CHOICES
from lieder.apps.misc import mlang


class Programme (meta.Model):
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
    intro.short_description = _('introduction')

    default_first_part= meta.TextField (_('first part'), editable=False,)
    default_first_part_markup = meta.TextField (_('first part'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def first_part(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'first_part')
    first_part.short_description = _('first part')

    default_second_part= meta.TextField (_('second part'), editable=False,)
    default_second_part_markup = meta.TextField (_('second part'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def second_part(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'second_part')
    second_part.short_description = _('second part')

    default_footer= meta.TextField (_('footer'), editable=False,)
    default_footer_markup = meta.TextField (_('footer'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def footer(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'footer')
    footer.short_description = _('footer')


    pub_date = meta.DateTimeField (_('publication date'),)
    slug = meta.SlugField (_('permalink'),
        prepopulate_from = ('default_name',),
        unique = True,
        help_text = _('Name to be linked'),
        )


    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup (self)
        
    def __repr__ (self):
        return self.default_name

    def get_absolute_url (self):
        pass


    class META:
        verbose_name = _('programme')
        verbose_name_plural = _('programmes') 
        admin = meta.Admin(
            fields=(
            (None, {'fields': ('default_name',)}),
            (_('Introduction'), {'fields': ('default_intro_markup',),
                        'classes': 'collapse',}),
            (None, {'fields': ('default_first_part_markup',
                    'default_second_part_markup', 'pub_date',)}),
            (_('Footer'), {'fields': ('default_footer_markup',),
                        'classes': 'collapse',}),
            (_('Advanced'), {'fields': ('slug',),
                          'classes': ('collapse',)} ),
            ),
        )

class Name (CharTranslation):
    parent = meta.ForeignKey(Programme, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for name')
        verbose_name_plural = _('translations for names')

class Intro (TextTranslation):
    parent = meta.ForeignKey(Programme, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for introduction')
        verbose_name_plural = _('translations for introduction')

class First_part (TextTranslation):
    parent = meta.ForeignKey(Programme, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for First_part')
        verbose_name_plural = _('translations for First_parts')

class Second_part (TextTranslation):
    parent = meta.ForeignKey(Programme, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for Second_part')
        verbose_name_plural = _('translations for Second_parts')

class Footer (TextTranslation):
    parent = meta.ForeignKey(Programme, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for Footer')
        verbose_name_plural = _('translations for Footers')
