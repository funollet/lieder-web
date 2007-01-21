from django.db import models
from django.utils.translation import gettext_lazy as _
from misc import markup
from misc.mlang import CharTranslation, TextTranslation, CHOICES
from misc import mlang


class Concert (models.Model):
    pub_date = models.DateTimeField (_('Unpublication date'), )
    
    default_start_date = models.CharField (_('concert start date'), maxlength=200, )

    def start_date(self):
        from misc import mlang
        return mlang.get_text(self, 'start_date')
    start_date.short_description = _('start date')
    
    default_city = models.CharField (_('city'), maxlength=200, )

    def city(self):
        from misc import mlang
        return mlang.get_text(self, 'city')
    city.short_description = _('city')

    default_auditorium = models.CharField (_('auditorium'), maxlength=200, blank=True, )

    def auditorium(self):
        from misc import mlang
        return mlang.get_text(self, 'auditorium')
    auditorium.short_description = _('auditorium')

    default_address = models.CharField (_('address'), maxlength=200, blank=True, )

    def address(self):
        from misc import mlang
        return mlang.get_text(self, 'address')
    address.short_description = _('address')

    default_cycle = models.CharField (_('cycle'), maxlength=200, blank=True, )

    def cycle(self):
        from misc import mlang
        return mlang.get_text(self, 'cycle')
    cycle.short_description = _('cycle')

    default_programme = models.CharField (_('programme'), maxlength=200, blank=True, )

    def programme(self):
        from misc import mlang
        return mlang.get_text(self, 'programme')
    programme.short_description = _('programme')

    default_tickets = models.CharField (_('tickets'), maxlength=200, blank=True, )

    def tickets(self):
        from misc import mlang
        return mlang.get_text(self, 'tickets')
    tickets.short_description = _('tickets')

    default_price = models.CharField (_('price'), maxlength=200, blank=True, )

    def price(self):
        from misc import mlang
        return mlang.get_text(self, 'price')
    price.short_description = _('price')

    default_organization = models.CharField (_('organization'), maxlength=200, blank=True, )

    def organization(self):
        from misc import mlang
        return mlang.get_text(self, 'organization')
    organization.short_description = _('organization')

    default_others= models.TextField (_('others'), editable=False,)
    default_others_markup = models.TextField (_('others'), 
        blank=True,
        help_text = markup.MARKUP_HELP,
        )

    def others(self):
        from misc import mlang
        return mlang.get_text(self, 'others')
    others.short_description = _('others')


    slug = models.SlugField (_('permalink'),
        prepopulate_from = ('default_city', 'default_start_date', 'default_auditorium',),
        help_text = _('Name to be linked'),
        )

    def __str__ (self):
        return ' :: '.join((self.default_city, self.default_start_date, ))

    def save (self):
        from misc import markup
        markup.parse_markup(self)
        super(Concert, self).save()

    def get_absolute_url (self):
        pass

    class Meta:
        verbose_name = _('concert')
        verbose_name_plural = _('concerts')
        ordering = ['pub_date']
    class Admin:
        list_display = ('default_city', 'default_auditorium', 'default_start_date',
                        'default_cycle', 'default_programme')
        list_filter = ('default_city', 'default_cycle', 'default_programme')
        fields = (
            (None, {
                'fields': ('default_start_date', 'default_city',
                'default_auditorium', 'default_address', 'default_cycle',
                'default_programme', 'default_tickets', 'default_price',
                'default_organization', 'pub_date'),
                'classes': 'liederWideInput',
            }),
            ('Altres', {
                'fields': ('default_others_markup', 'slug'),
                'classes': 'collapse',
            }),
        )

class start_date (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for start_date')
        verbose_name_plural = _('translations for start_dates')


class city (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for city')
        verbose_name_plural = _('translations for citys')

class auditorium (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for auditorium')
        verbose_name_plural = _('translations for auditoriums')

class address (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for address')
        verbose_name_plural = _('translations for address')

class cycle (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for cycle')
        verbose_name_plural = _('translations for cycles')

class programme (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for programme')
        verbose_name_plural = _('translations for programmes')

class tickets (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for tickets')
        verbose_name_plural = _('translations for tickets')

class price (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for price')
        verbose_name_plural = _('translations for prices')

class organization (CharTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1, 
       max_num_in_admin=len(CHOICES))
    class Meta:
        verbose_name = _('translation for organization')
        verbose_name_plural = _('translations for organizations')

class others (TextTranslation):
    parent = models.ForeignKey(Concert, edit_inline=models.TABULAR, num_in_admin=1,
        max_num_in_admin=len(CHOICES))

    class Meta:
        verbose_name = _('translation for others')
        verbose_name_plural = _('translations for others')
