from django.core import meta
from django.utils.translation import gettext_lazy as _
from django.conf.settings import LANGUAGES, LANGUAGE_CODE, DEBUG
#import re
from lieder.apps.misc import misc

CHOICES = []
LANGUAGES_DICT = dict(LANGUAGES)
def _setup():
    global CHOICES
    for code, name in LANGUAGES:
        if LANGUAGE_CODE != code:
            CHOICES.append((code, name))

_setup()
del _setup


# _BR_CLEANUP = re.compile(r'<\s*br\s*/?\s*>', re.IGNORECASE)
# 
# def text_cleanup(txt, clean_br=True, cleanup_double_space=True, strip_ws=True):
#     if txt:
#         if clean_br:
#             txt = _BR_CLEANUP.sub(' ', txt) # remove <br />
#         #
#         
#         if strip_ws:
#             txt = txt.strip() # strip all leading/trailing spaces
#         #
#         
#         if cleanup_double_space:
#             while '  ' in txt: txt = txt.replace('  ', ' ') # remove double spaces
#         #
# 
#         return txt
#     else:
#         return txt


class CharTranslation(meta.Model):
    if len(CHOICES) == 1:
        language = meta.CharField(_('language'), maxlength=4, choices=CHOICES,
                                  default=CHOICES[0][0], db_index=True)
    else:
        language = meta.CharField(_('language'), maxlength=4, choices=CHOICES,
                                  db_index=True)

    text = meta.CharField(_('text'), maxlength=255, core=True)

    def __repr__(self):
        lang = self.language
        return '[%s] %s' % (self.language, self.text)

    class META:
        unique_together = (('parent', 'language'),)


class TextTranslation(meta.Model):
    if len(CHOICES) == 1:
        language = meta.CharField(_('language'), maxlength=4, choices=CHOICES, default=CHOICES[0][0], db_index=True)
    else:
        language = meta.CharField(_('language'), maxlength=4, choices=CHOICES, db_index=True)

    text = meta.TextField(_('text raw'), editable=False, blank=True,)
    text_markup = meta.TextField(_('text markup'), core=True,
        help_text = misc.MARKUP_HELP,)

    def __repr__(self):
        lang = self.language
        return '[%s] %s' % (self.language, self.text_markup)

    def _pre_save (self):
        from lieder.apps.misc import misc
        misc.parse_markup (self)


    class META:
        unique_together = (('parent', 'language'),)
#         admin = meta.Admin(
#             fields = (
#             (None, {'fields': ('text_markup', 'language',),}),
#         ),)





from django.utils.translation import get_language, gettext
from django.core.exceptions import ObjectDoesNotExist

def get_text(obj, field, table=None, language=None, fallback=None):
    ret = ''
    if not language:
        language = get_language()

    if LANGUAGE_CODE == language:
        ret = getattr(obj, 'default_%s' % field)
    else:
        if table is None:
            getobj = getattr(obj, 'get_%s' % field)
        else:
            getobj = getattr(obj, 'get_%s' % table.lower())
        try:
            ret = getobj(language__exact=language).text
        except ObjectDoesNotExist, err:
            pass


    if not ret:
        ret = getattr(obj, 'default_%s' % field)
        if not ret and fallback is not None:
            ret = fallback
        else:
            ret = getattr(obj, 'default_%s' % field)

    return ret




def translated_for(obj, field, table=None, add_default=True):
    if table is not None:
        fld = table.lower()
    else:
        fld = field
    try:
        default = getattr(obj, 'default_%s' % field, None)
        if default:
            if add_default:
                lst = [LANGUAGE_CODE]
        else:
            lst = []


        lst += [n.language for n in getattr(obj, 'get_%s_list' % fld.replace('_', ''))() if n.text]
        return ', '.join([str(LANGUAGES_DICT[t]) for t in lst])
    except Exception, err:
        if DEBUG:
            return str(err)
        else:
            raise
