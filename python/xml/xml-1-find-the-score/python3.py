import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return len(node.items()) + sum([get_attr_number(x) for x in node])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))