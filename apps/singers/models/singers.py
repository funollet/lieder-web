from django.core import meta
from django.utils.translation import gettext_lazy as _


VOICE_CHOICES = (
    ('sopranos', _('sopranos')),
    ('altos', _('altos')),
    ('tenors', _('tenors')),
    ('basses', _('basses')),
    )


class Singer (meta.Model):
    name = meta.CharField(_('name'), maxlength=200, )
    voice = meta.CharField(_('voice'), maxlength=200,
        choices = VOICE_CHOICES, )

    def __repr__(self):
        return self.name

    class META:
        verbose_name = _('singer')
        verbose_name_plural = _('singers')
        ordering = ['name']
        admin = meta.Admin(
            list_filter = ('voice',),
            search_fields = ('name',),
            )
        
