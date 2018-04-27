# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 15:04:43 2018

@author: ee15sjm
"""

from lxml import etree

#open dtd file
dtd_file = open("map1.dtd")
#open xml file
xml1 = open("map1.xml").read()
#remove .xml prolog to prevent lxml objecting to it
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")

dtd = etree.DTD(dtd_file)
root = etree.XML(xml1)
print(dtd.validate(root))

#list xml elements
print (root.tag)			# "map"
print (root[0].tag)			# "polygon"
print (root[0].get("id"))		# "p1"
print (root[0][0].tag)		# "points"
print (root[0][0].text)

#add new polygon and list elements
p2 = etree.Element("polygon")				# Create polygon
p2.set("id", "p2");					# Set attribute
p2.append(etree.Element("points"))			# Append points
p2[0].text = "100,100 100,200 200,200 200,100"	# Set points text
root.append(p2)						# Append polygon
print (root[1].tag)
print (root[1].get("id"))		# "p1"
print (root[1][0].tag)		# "points"
print (root[1][0].text)

#write to file
out = etree.tostring(root, pretty_print=True)
print(out)
writer = open('xml3.xml', 'wb')		# Open for binary write
writer.write(out)
writer.close()


#convert to html
xsl3 = open("map3.xsl").read()		# Read stylesheet
#xsl3 = xsl3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")

xslt_root = etree.XML(xsl3)			# Parse stylesheet
transform = etree.XSLT(xslt_root)		# Make transform
result_tree = transform(root)			# Transform some XML root
transformed_text = str(result_tree)

print(transformed_text)
writer = open('map4.html', 'w')		# Normal writer
writer.write(transformed_text)
