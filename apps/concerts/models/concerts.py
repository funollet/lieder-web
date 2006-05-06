from django.core import meta
from django.utils.translation import gettext_lazy as _
from lieder.apps.misc import misc
from lieder.apps.misc.mlang import CharTranslation, TextTranslation, CHOICES
from lieder.apps.misc import mlang


class Concert (meta.Model):
    start_date = meta.DateTimeField (_('start time'), )
    
    default_city = meta.CharField (_('city'), maxlength=200, )

    def city(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'city')
    city.short_description = _('city')

    default_auditorium = meta.CharField (_('auditorium'), maxlength=200, blank=True, )

    def auditorium(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'auditorium')
    auditorium.short_description = _('auditorium')

    default_address = meta.CharField (_('address'), maxlength=200, blank=True, )

    def address(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'address')
    address.short_description = _('address')

    default_cycle = meta.CharField (_('cycle'), maxlength=200, blank=True, )

    def cycle(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'cycle')
    cycle.short_description = _('cycle')

    default_programme = meta.CharField (_('programme'), maxlength=200, blank=True, )

    def programme(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'programme')
    programme.short_description = _('programme')

    default_tickets = meta.CharField (_('tickets'), maxlength=200, blank=True, )

    def tickets(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'tickets')
    tickets.short_description = _('tickets')

    default_price = meta.CharField (_('price'), maxlength=200, blank=True, )

    def price(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'price')
    price.short_description = _('price')

    default_organization = meta.CharField (_('organization'), maxlength=200, blank=True, )

    def organization(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'organization')
    organization.short_description = _('organization')

    default_others= meta.TextField (_('others'), editable=False,)
    default_others_markup = meta.TextField (_('others'), 
        blank=True,
        help_text = misc.MARKUP_HELP,
        )

    def others(self):
        from lieder.apps.misc import mlang
        return mlang.get_text(self, 'others')
    others.short_description = _('others')


    slug = meta.SlugField (_('slug'), unique_for_date = 'start_date',
        prepopulate_from = ('default_city', 'start_date'),
        help_text = _('Readable link name'),
        )

    def __repr__ (self):
        return ' :: '.join((self.default_city, str(self.start_date.date()), ))

    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup(self)


    class META:
        verbose_name = _('concert')
        verbose_name_plural = _('concerts')
        admin = meta.Admin(
            list_display = ('default_city', 'default_auditorium', 'start_date',
                            'default_cycle', 'default_programme'),
            list_filter = ('default_city', 'default_cycle', 'default_programme'),
            )


class city (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for city')
        verbose_name_plural = _('translations for citys')

class auditorium (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for auditorium')
        verbose_name_plural = _('translations for auditoriums')

class address (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for address')
        verbose_name_plural = _('translations for address')

class cycle (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for cycle')
        verbose_name_plural = _('translations for cycles')

class programme (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for programme')
        verbose_name_plural = _('translations for programmes')

class tickets (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for tickets')
        verbose_name_plural = _('translations for tickets')

class price (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for price')
        verbose_name_plural = _('translations for prices')

class organization (CharTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class META:
        verbose_name = _('translation for organization')
        verbose_name_plural = _('translations for organizations')

class others (TextTranslation):
    parent = meta.ForeignKey(Concert, edit_inline=meta.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class META:
        verbose_name = _('translation for others')
        verbose_name_plural = _('translations for others')
