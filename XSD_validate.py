# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 15:19:14 2018

@author: ee15sjm
"""

from lxml import etree

#open xsd file
xsd_file = open("map2.xsd")
#open xml file
xml2 = open("map2.xml").read()

#remove prolog to avoid lxml objecting
xml2 = xml2.replace('<?xml version="1.0" encoding="UTF-8"?>',"")

#parse the xsd xml
xsd = etree.XMLSchema(etree.parse(xsd_file))

root = etree.XML(xml2)
print(xsd.validate(root))