import urllib2
import sys
import os

from HTMLParser import HTMLParser

class StyleTileParser(HTMLParser):
    """
    Scans a chunk of HTML and trims it down to tags classes and IDs
    """
    depth = 0
    indent_width = 2
    output = []
    tags_to_ignore = ['meta','style','strong','em','b','i','br']
    self_closing_tags = ["area", "base", "basefont", "br", "col", "frame", "hr", "img", "input", "link", "meta", "param"]

    def __init__(self):
        HTMLParser.__init__(self)

    def tag_parser(self, tag, attributes):
        if tag in self.tags_to_ignore:
            return

        attrs = dict(attributes)
        output = " " * (self.indent_width * self.depth) + tag

        if attrs.has_key('id'):
            output += "#" + attrs['id']

        if attrs.has_key('class'):
            classes = attrs['class'].split()
            output += "." + ".".join(classes)
    
        if tag == 'div' and len(attrs) == 0:
            output += "    <<-- Div with no attributes"

        return output
 
    def handle_starttag(self, tag, attrs):

        output = self.tag_parser(tag,attrs) 
        if output:
            self.output.append(output)
            if tag not in self.self_closing_tags:
                self.depth += 1

    def handle_startendtag(self, tag, attrs):

        output = self.tag_parser(tag,attrs) 
        if output:
            self.output.append(output)

    def handle_endtag(self, tag):
        if tag in self.tags_to_ignore:
            return
        if self.depth != 0:
            self.depth -= 1
        else:
            raise Exception("Depth level error - too many close tags")

    def handle_data(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

f = sys.stdin
for arg in sys.argv[1:]:
    print "Using html from %s" % arg
    if arg.startswith("http"):
        f = urllib2.urlopen(arg)
    else:
        f = open(arg, 'r')
    break

html = f.read()
f.close()
parser = StyleTileParser()
parser.feed(html)
if len(parser.output):
    print "\n".join(parser.output)
else:
    print "No output"

