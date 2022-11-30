import xml.dom.minidom as minodom
import xml.etree.cElementTree as ET
import csv
import pandas as pd
import os


def get_files_xml(path_to_files):
    return os.listdir(path_to_files)


def parse_xml(xml_file):
    doc = minodom.parse(xml_file)
    # data = []
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
    # return data


if __name__ == "__main__":
    PATH_TO_FILE = os.path.join(os.getcwd(), 'XML')

    list_of_files = get_files_xml(PATH_TO_FILE)
    print(list_of_files)

    for file in list_of_files:
        full_path = PATH_TO_FILE + file
        print(full_path)

        # df = (get_dataframe(parse_xml(full_path)))
        # dfs.append(df)
        # multiple_dfs(dfs, 'Kievstar', 'output.xlsx', 1)
