# misc.py
# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _


MARKDOWN_HELP = _('Use <a href="http://daringfireball.net/projects/markdown/basics">Markdown</a> Syntax')
TEXTILE_HELP = _('Use <a href="http://daringfireball.net/projects/markdown/basics">Textile</a> Syntax')
DOCUTILS_HELP = _('Use <a href="http://docutils.sourceforge.net/docs/user/rst/quickstart.html">reST</a> Syntax')
MARKUP_HELP = DOCUTILS_HELP



def parse_markup (obj):
    """Parses markup attributes and pre-saves as HTML.
    
    Reads all obj.xxx_markup attributes and saves at obj.xxx,
    transformed into HTML. Uses a bit of instrospection. Allows
    choosing which markup to use.

    Parameters::
        
        ``obj``:              object to parse
        ``settings.MARKUP``:  one of <docutils,markdown,textile>
    """

    TAIL='_markup'      # Suffix for names of attributes containing markup.

    from django.conf.settings import MARKUP

    # Choose a markup parser.
    if MARKUP=='docutils':
        from docutils.core import publish_parts
        # commandline troubleshooting
        # echo ç | rst2html -o ascii --output-encoding-error-handler xmlcharrefreplace -
#         docutils_settings = {}
#         docutils_settings = {
#             'input_encoding': 'unicode',
#             'output_encoding': 'unicode',
#             'output-encoding-error-handler': 'xmlcharrefreplace'}
        parse = lambda s: publish_parts (source=s, writer_name="html4css1")["fragment"].encode('utf-8')
    elif MARKUP == 'markdown':
        import markdown
        parse = lambda s: markdown.markdown(s)
    elif MARKUP == 'textile':
        import textile
        parse = lambda s: textile.textile(s)
    else:
        raise ImportError("Incorrect value for django.conf.settings.MARKUP")


    def conditions (s):
        """Select non-hidden %s-ended strings""" % TAIL
        return ( s.endswith(TAIL) and not s.startswith('_') )

    markup_fields = [field for field in dir(obj) if conditions(field)]

    for longname in markup_fields :
        # Example: longname = 'first_part_markup'
        shortname = longname[:-len(TAIL)]
        # Example: shortname = 'first_part'
        markup_source = getattr(obj, longname)
        setattr(obj, shortname, parse(markup_source))
        # Example: self.first_part = parse (self.first_part_markup)
