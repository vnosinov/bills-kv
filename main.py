import xml.dom.minidom as minodom
import xml.etree.cElementTree as ET
import csv
import pandas as pd
import os
from pprint import pprint


def get_files_xml(path_to_files):
    return os.listdir(path_to_files)


def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data_dict = {}

    for member in root.iter('Invoice'):
        for obj in member.findall('Customer'):
            for obj1 in obj.findall('BillingAccount'):
                billing_account = obj1.text
                data_dict[billing_account] = []

        for contract_detail in member.findall('Contract/ContractDetail'):
            contract_id = contract_detail.find('ContractID')
            for total_amount in contract_detail.findall('SubInvoiceAmount/AmountDetail/TotalAmount'):
                pair_data = (billing_account, contract_id.text, float(total_amount.text))
                data_dict[billing_account].append(pair_data)
    return data_dict


def stat_data(data_dict):
    my_list = []
    for key in data_dict.keys():
        if key not in ['5210888', '5209074']:
            for i in data_dict[key]:
                bill_acc, cont_id, total_am = i

                my_list.append([bill_acc, cont_id, str(total_am).replace('.', ',')])

    df = pd.DataFrame(my_list, columns=['bill', 'number', 'amount'])
    writer = pd.ExcelWriter('output.xlsx')

    df.to_excel(writer)  # save the excel
    writer.save()
    print('DataFrame is written successfully to Excel File.')


if __name__ == "__main__":
    PATH_TO_FILE = os.path.join(os.getcwd(), 'XML\\')
    list_of_files = get_files_xml(PATH_TO_FILE)
    full_path = PATH_TO_FILE + list_of_files[0]
    xml_dict = parse_xml(full_path)

    stat_data(xml_dict)

