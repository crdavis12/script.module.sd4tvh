__author__ = 'edit4ever'

def indent(elem, level=0):
    """
    http://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
    :param elem:
    :param level:
    :return:
    """
    i = u"\n" + level * u" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + u" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

from xmltv.xmltvdocument import XmltvDocument
from xmltv.xmltvchannel import XmltvChannel
from xmltv.xmltvprogramme import XmltvProgramme
from xmltv.xmltvwriter import XmltvWriter
