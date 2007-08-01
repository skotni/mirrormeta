#!/usr/bin/env python
#
# Example: cat foo.metalink bar.metalink | ./metalinkmerge.py > merged.metalink
# concatenates foo.metalink and bar.metalink to merged.metalink
# All but <file> tags is lost!

import string, sys
import xml.dom.minidom

def parse(doc, outnode):
	dom = xml.dom.minidom.parseString(doc)
	for file in dom.getElementsByTagName('file'):
		outnode.appendChild(file)

dom = xml.dom.minidom.Document()

metalink = dom.createElementNS('http://www.metalinker.org/', 'metalink')
metalink.setAttribute('xmlns', 'http://www.metalinker.org/') # TODO: force xmlns in a nicer fashion 
metalink.setAttribute('version', '3.0')
files = dom.createElement('files')

doc = sys.stdin.readline()
for line in sys.stdin:
	if string.find(line, '<?xml') != -1:
		parse(doc, files)
		doc = line
	else:
		doc += line

parse(doc, files)

metalink.appendChild(files)
dom.appendChild(metalink)
print dom.toxml()