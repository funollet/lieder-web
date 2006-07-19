from docutils import writers
from docutils.writers import html4css1

class Writer(html4css1.Writer):
    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = DjangoHTMLTranslator


class DjangoHTMLTranslator(html4css1.HTMLTranslator):
    def visit_table(self, node):
        self.body.append(
            self.starttag(node, 'table', CLASS='docutils'))

    def write_colspecs(self):
        idx = 0
        for node in self.colspecs:
            self.body.append(self.starttag(node, 'col',
                                           CLASS='col-%s' % idx))
            idx += 1 
        self.colspecs = []
