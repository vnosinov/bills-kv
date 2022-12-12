import xml.etree.cElementTree as ET
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

            amount_id = contract_detail.findall('Summary/SummaryRow/RowDetail/Summary/SummaryRow/RowDetail/Id')
            amount = contract_detail.findall('Summary/SummaryRow/RowDetail/Summary/SummaryRow/RowDetail/Amount')

            for i, e in zip(amount_id, amount):
                if i.text == '1':

                    abon_amount = float(e.text)

            for total_amount in contract_detail.findall('SubInvoiceAmount/AmountDetail/TotalAmount'):
                pair_data = (billing_account, contract_id.text, float(total_amount.text), abon_amount)
                data_dict[billing_account].append(pair_data)

    return data_dict


def stat_data(data_dict):
    my_list = []
    for key in data_dict.keys():
        if key not in ['5210888', '5209074']:
            for i in data_dict[key]:
                bill_acc, cont_id, total_am, abon_am = i
                # print(bill_acc, cont_id, total_am, abon_am)
                my_list.append([bill_acc, cont_id, str(total_am).replace('.', ','), str(abon_am).replace('.', ',')])

    df = pd.DataFrame(my_list, columns=['bill', 'number', 'amount', 'abon'])
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer)  # save the excel
        print('DataFrame is written successfully to Excel File.')


if __name__ == "__main__":
    PATH_TO_FILE = os.path.join(os.getcwd(), 'XML\\')
    list_of_files = get_files_xml(PATH_TO_FILE)
    full_path = PATH_TO_FILE + list_of_files[1]
    # print(full_path)
    xml_dict = parse_xml(full_path)
    # pprint(xml_dict)
    stat_data(xml_dict)

