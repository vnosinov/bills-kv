import xml.dom.minidom as minodom
import xml.etree.cElementTree as ET
import csv
import pandas as pd
import os


def get_files_xml(path_to_files):
    return os.listdir(path_to_files)


def parse_xml(xml_file):
    data = []
    doc = minodom.parse(xml_file)
    contract_detail = doc.getElementsByTagName('ContractDetail')
    billing_account = doc.getElementsByTagName('BillingAccount')

    # customer = doc.getElementsByTagName('Customer')
    # for i, bill in enumerate(customer):
    #     billing_account = doc.getElementsByTagName('BillingAccount')[::].firstChild.data
    #     print(i+1, billing_account)

    for i, cont in enumerate(contract_detail):
        contract_id = cont.getElementsByTagName('ContractID')[0].firstChild.data
        total_amount = cont.getElementsByTagName('TotalAmount')[0].firstChild.data
        data.append((contract_id, total_amount))
        # print(i+1, contract_id, total_amount)


    # for i, bill in enumerate(billing_account):
    #
    #
    #     # contract_id = cont.getElementsByTagName('ContractID')[0].firstChild.data
    #     # total_amount = cont.getElementsByTagName('TotalAmount')[0].firstChild.data
    #     # print(i+1, contract_id, total_amount)



    # print(contract_detail)
    # account = doc.getElementsByTagName('Account_No')[0].firstChild.data
    # bill_data = doc.getElementsByTagName('BillDate')[0].firstChild.data
    # lst = doc.getElementsByTagName("Device")
    #
    # for device in lst:
    #     sa = device.getElementsByTagName('ServiceAgreement')[0].firstChild.data
    #     dmaoc = device.getElementsByTagName('DeviceMonthlyAndOtherCharges')[0].firstChild.data
    #     dc = device.getElementsByTagName('DeviceCalls')[0].firstChild.data
    #     deoc = device.getElementsByTagName('DeviceOtherCharges')[0].firstChild.data
    #     drs = device.getElementsByTagName('DeviceRoamingServices')[0].firstChild.data
    #     dtwt = device.getElementsByTagName('DeviceTotalWithTaxes')[0].firstChild.data
    #     dfcs = device.getElementsByTagName('DeviceFixedCallsSummary')[0].firstChild.data
    #     dtfp = device.getElementsByTagName('DeviceTotalForPeriod')[0].firstChild.data
    #
    #     data.append((bill_data, account, sa, dmaoc, dc, deoc, drs, dtwt, dfcs, dtfp))
    #
    return data


# if __name__ == "__main__":
#     PATH_TO_FILE = os.path.join(os.getcwd(), 'XML/')
#
#     list_of_files = get_files_xml(PATH_TO_FILE)
#     # print(list_of_files)
#
#     for file in list_of_files:
#         full_path = PATH_TO_FILE + file
#         print(parse_xml(full_path))
#
#         # df = (get_dataframe(parse_xml(full_path)))
#         # dfs.append(df)
#         # multiple_dfs(dfs, 'Kievstar', 'output.xlsx', 1)
