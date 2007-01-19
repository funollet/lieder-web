# rst2django
# Customized writer for docutils. Default html4ccs1 writers creates
# ugly tables with border=1 and a self-decided width.

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
	    # Overrides:
            #self.starttag(node, 'table', CLASS='docutils', border="1"))

    def write_colspecs(self):
        idx = 0
        for node in self.colspecs:
            self.body.append(self.starttag(node, 'col', CLASS='col-%s' % idx))
            idx += 1 
        self.colspecs = []
    
    # Overrides:
    #def write_colspecs(self):
        #width = 0
        #for node in self.colspecs:
            #width += node['colwidth']
        #for node in self.colspecs:
            #colwidth = int(node['colwidth'] * 100.0 / width + 0.5)
            #self.body.append(self.emptytag(node, 'col',
                                           #width='%i%%' % colwidth))
        #self.colspecs = []

