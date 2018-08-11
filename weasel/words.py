simplicity = [ 'basic', 'simple', 'easy', 'special', 'new' ]
importance = [ 'flexible', 'extended', 'smart', 'optimized',
               'advanced', 'abstract', 'general', 'super', 'core']
party_hats = [ '^my', '^the' ]
hungarian = [ 'interface', 'struct', 'impl', 'class', 'object' ]

import ast
import os
import re
import sys

class WeaselClassNamePattern(ast.NodeVisitor):
    def __init__(self):
        ast.NodeVisitor.__init__(self)
        weasel_word_list = simplicity + importance + party_hats + hungarian
        self.name_pattern = re.compile('|'.join(weasel_word_list), re.I)
        self.camel_case_pattern = re.compile('[A-Z][^A-Z]*') # split camel case

    def visit_ClassDef(self, node):
        for class_name_part in self.camel_case_pattern.findall(node.name):
            m = self.name_pattern.search(class_name_part)
            if m:
                print "weasel word in classname \"%s\" found, line %d" % \
                    (node.name, node.lineno)

        for statement in node.body:
            self.visit(statement)

def main(argv):
    if len(argv) < 2:
        print >>sys.stderr, "usage", argv[0], "<directory>"
        sys.exit(1)

    file_name_pattern = re.compile(r'\.py$')

    for root, dirs, files in os.walk(argv[1]):
        for name in files:
            filename = os.path.join(root, name)

            if not file_name_pattern.search(filename):
                continue

            print filename

            with open(filename, 'r') as f:
                try:
                    WeaselClassNamePattern().visit(ast.parse(f.read()))
                except SyntaxError:
                    pass # ignore
