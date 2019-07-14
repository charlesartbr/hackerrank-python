from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  
    def handle_comment(self, data):
        print('>>> %s-line Comment' % ('Multi' if data.find('\n') > 0 else 'Single'))
        print(data)
  
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
  

html = str.join('\n', [input().rstrip() for _ in range(int(input()))])
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

