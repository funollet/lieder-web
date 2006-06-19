from django.db import models
from django.utils.translation import gettext_lazy as _


VOICE_CHOICES = (
    ('sopranos', _('sopranos')),
    ('altos', _('altos')),
    ('tenors', _('tenors')),
    ('basses', _('basses')),
    )


class Singer (models.Model):
    name = meta.CharField(_('name'), maxlength=200, )
    voice = meta.CharField(_('voice'), maxlength=200,
        choices = VOICE_CHOICES, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('singer')
        verbose_name_plural = _('singers')
        ordering = ['name']
    class Admin:
        list_filter = ('voice',)
        search_fields = ('name',)
