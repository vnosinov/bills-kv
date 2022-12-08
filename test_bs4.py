from main import get_files_xml
import bs4
import os
from lxml import etree
import xml.etree.ElementTree as ET
from pprint import pprint


def get_bills():
    my_dict = {}
    path_to_file = os.path.join(os.getcwd(), 'XML\\')
    filename = os.listdir(path_to_file)[1]
    # print(filename)
    full_path = os.path.join(path_to_file, filename)
    tree = ET.parse(full_path)
    root = tree.getroot()
    print(root)
    # xml = full_path
    events = ("start", "end", "start-ns", "end-ns")

    number = None

    for event, elem in ET.iterparse(full_path, events=events):

        if elem.tag == "BillingAccount" and event == "end":
            bill = elem.text
            my_dict[bill] = []

        elif elem.tag == 'ContractID' and event == "end":
            number = elem.text

        elif elem.tag == 'TotalAmount' and event == "end":
            summ = elem.text
            my_dict[bill].append((number, summ))



            # print(elem.text)

            elem.clear()
    pprint(my_dict)
        # print(event)

    # for child in root:
    #     print(child.tag, child.attrib)
    #
    #     bill = child[0][1].text
    #     print(bill)
    #
    #
    #
    #     # for event, elem in ET.iterparse(child, events=events):
    #     #     if elem.tag == "BillingAccount" and event == "end":
    #     #         print(elem.text)
    #     #
    #
    #



if __name__ == "__main__":
    get_bills()

