from main import get_files_xml
import bs4
import os


def get_bills():

    path_to_file = os.path.join(os.getcwd(), 'XML\\')
    filename = os.listdir(path_to_file)[0]
    soup = bs4.BeautifulSoup
    full_path = os.path.join(path_to_file, filename)

    with open(full_path) as f:
        src = f.read()
    print(src)
    # print(path_to_file, filename, full_path)


if __name__ == "__main__":
    get_bills()

