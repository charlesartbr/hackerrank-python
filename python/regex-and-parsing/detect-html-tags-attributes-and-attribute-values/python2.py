from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def print_attrs(self, attrs):
        for attr in attrs:
            print "->", attr[0], ">", attr[1]

    def handle_starttag(self, tag, attrs):
        print tag
        self.print_attrs(attrs)

    def handle_comment(self, data):
        pass
    
    def handle_startendtag(self, tag, attrs):
        print tag
        self.print_attrs(attrs)

n = int(raw_input())

html = ''

for _ in xrange(n):
    html += raw_input()

parser = MyHTMLParser()
parser.feed(html)