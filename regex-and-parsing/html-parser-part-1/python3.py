from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def print_attrs(self, attrs):
        [print("->", attr[0], ">", attr[1]) for attr in attrs]

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.print_attrs(attrs)

    def handle_comment(self, data):
        pass
        
    def handle_endtag(self, tag):
        print("End   :", tag)
    
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.print_attrs(attrs)

html = str.join('', [input() for _ in range(int(input()))])

parser = MyHTMLParser()
parser.feed(html)