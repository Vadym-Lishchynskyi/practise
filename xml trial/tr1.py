# -*- coding: utf-8 -*-
import xml.etree.ElementTree as xml


def createXML(filename):
    """
    Создаем XML файл.
    """
    configuration = xml.Element("configuration")
    appSettings = xml.Element("appSettings")
    configuration.append(appSettings)

    # создаем дочерний суб-элемент.
    filepath = xml.SubElement(appSettings, "filepath")
    filepath.text = "1181251680"

    # subject = xml.SubElement(configuration, "subject")

    tree = xml.ElementTree(configuration)
    with open(filename, "wb") as fh:
        tree.write(fh)


if __name__ == "__main__":
    createXML("appt.xml")