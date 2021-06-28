import os
import xml.etree.ElementTree as ET
import platform

dateFormatter = '%Y-%m-%d-%H:%M'
error_message_for_commands = 'Command should be integer num from diapason above!\n'


def get_path_from_xml_config():
    print(os.path.join(os.getcwd()))
    tree = ET.parse(os.path.join(os.getcwd(), 'project', 'config.xml'))
    root = tree.getroot()

    if platform.system() == 'Windows':
        path = root[0][0].text
    else:
        # TODO remake point for linux and other oses
        path = root[0][1].text

    return path


path_to_test_data = os.path.join(os.getcwd(), get_path_from_xml_config(), 'test_data.txt')
# print(path_to_test_data)

# class Config:
#
