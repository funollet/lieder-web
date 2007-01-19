from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
#import re
from misc import misc

CHOICES = []
LANGUAGES_DICT = dict(settings.LANGUAGES)
def _setup():
    global CHOICES
    for code, name in settings.LANGUAGES:
        if settings.LANGUAGE_CODE != code:
            CHOICES.append((code, name))

_setup()
del _setup



class CharTranslation(models.Model):
    if len(CHOICES) == 1:
        language = models.CharField(_('language'), maxlength=4, choices=CHOICES,
                                  default=CHOICES[0][0], db_index=True)
    else:
        language = models.CharField(_('language'), maxlength=4, choices=CHOICES,
                                  db_index=True)

    text = models.CharField(_('text'), maxlength=255, core=True)

    def __str__(self):
        lang = self.language
        return '[%s] %s' % (self.language, self.text)

    class Meta:
        unique_together = (('parent', 'language'),)


class TextTranslation(models.Model):
    if len(CHOICES) == 1:
        language = models.CharField(_('language'), maxlength=4, choices=CHOICES, default=CHOICES[0][0],
            db_index=True)
    else:
        language = models.CharField(_('language'), maxlength=4, choices=CHOICES, db_index=True)

    text = models.TextField(_('text raw'), editable=False, blank=True,)
    text_markup = models.TextField(_('text markup'), core=True,
        help_text = misc.MARKUP_HELP,)

    def __str__(self):
        lang = self.language
        return '[%s] %s' % (self.language, self.text_markup)

    def save (self):
        from misc import misc
        misc.parse_markup (self)
        super (TextTranslation, self).save()


    class Meta:
        unique_together = (('parent', 'language'),)



from django.utils.translation import get_language, gettext
from django.core.exceptions import ObjectDoesNotExist

def get_text(obj, field, table=None, language=None, fallback=None):
    ret = ''
    if not language:
        language = get_language()

    if settings.LANGUAGE_CODE == language:
        ret = getattr(obj, 'default_%s' % field)
    else:
        if table is None:
            #getobj = getattr(obj, 'get_%s' % field)
            getobj = getattr(obj, '%s_set' % field)
        else:
            #getobj = getattr(obj, 'get_%s' % table.lower())
            getobj = getattr(obj, '%s_set' % table.lower())
        try:
            ret = getobj.filter(language__exact=language).get().text
        except ObjectDoesNotExist, err:
            pass


    if not ret:
        ret = getattr(obj, 'default_%s' % field)
        if not ret and fallback is not None:
            ret = fallback
        else:
            ret = getattr(obj, 'default_%s' % field)

    return ret



# not magic-removal-PROOF
def translated_for(obj, field, table=None, add_default=True):
    if table is not None:
        fld = table.lower()
    else:
        fld = field
    try:
        default = getattr(obj, 'default_%s' % field, None)
        if default:
            if add_default:
                lst = [settings.LANGUAGE_CODE]
        else:
            lst = []


        lst += [n.language for n in getattr(obj, 'get_%s_list' % fld.replace('_', ''))() if n.text]
        return ', '.join([str(LANGUAGES_DICT[t]) for t in lst])
    except Exception, err:
        if settings.DEBUG:
            return str(err)
        else:
            raise
