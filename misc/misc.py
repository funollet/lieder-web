# misc.py
# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _


MARKDOWN_HELP = _('Use <a href="http://daringfireball.net/projects/markdown/basics">Markdown</a> Syntax')
TEXTILE_HELP = _('Use <a href="http://daringfireball.net/projects/markdown/basics">Textile</a> Syntax')
DOCUTILS_HELP = ('''<pre>
`un link`_    *italica*    **negreta**    Titol     - un punt d'una llista
                                          -----     - segon punt
.. _`un link`: http://www.google.com                 - llista indentada
</pre>(Documentació completa de la <a href="http://docutils.sourceforge.net/docs/user/rst/quickstart.html">sintaxis reST</a>).''')
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

    from django.conf import settings

    # Choose a markup parser.
    if settings.MARKUP=='docutils':
        from docutils.core import publish_parts
	from misc.rst2django import Writer
        
        # commandline troubleshooting
        # echo ç | rst2html -o ascii --output-encoding-error-handler xmlcharrefreplace -
#         docutils_settings = {}
#         docutils_settings = {
#             'input_encoding': 'unicode',
#             'output_encoding': 'unicode',
#             'output-encoding-error-handler': 'xmlcharrefreplace'}
	djangowriter=Writer()
        overrides = {'initial_header_level': 2 }
        parse = lambda s: publish_parts (source=s, writer=djangowriter,
            settings_overrides=overrides)["fragment"].encode('utf-8')
    elif settings.MARKUP == 'markdown':
        import markdown
        parse = lambda s: markdown.markdown(s)
    elif settings.MARKUP == 'textile':
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
