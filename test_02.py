import xml.dom.minidom as minodom
from main import get_files_xml
import xml.etree.cElementTree as ET
import csv
import pandas as pd
import os
from pprint import pprint


def parse_xml1(filename):
    data_dict = {}
    dom = minodom.parse(filename)
    invoice = dom.getElementsByTagName('Invoice')
    # dom.normalize()

    for node in invoice:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Customer':
                    node_1 = child
                    for node_2 in node_1.childNodes:
                        if node_2.tagName == 'BillingAccount':
                            print(node_2)




                    # print(f'child = {child}')


if __name__ == "__main__":
    PATH_TO_FILE = os.path.join(os.getcwd(), 'XML\\')

    list_of_files = get_files_xml(PATH_TO_FILE)
    full_path = PATH_TO_FILE + list_of_files[1]
    print(full_path)
    parse_xml1(full_path)
