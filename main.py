# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import argparse
import datetime
import json

parser = argparse.ArgumentParser()

x = datetime.datetime.now()

default_tag = x.strftime("%Y%m%d%H%M%S")
default_type = "minor"
timestamp = x

parser.add_argument("-t", "--tag", dest="tag", default=default_tag, help="Image Tag")
parser.add_argument("-rt", "--type", dest="type", default=default_type, help="Release Type")
parser.add_argument('-cid', "--changelog", dest="changelog", default="0000", help="Change log Id")
parser.add_argument('-sn', "--service", dest="service", default="none", help="Service Name")
parser.add_argument('-pv', "--pversion", dest="pversion", default="none", help="Platform Version")
parser.add_argument('-pn', "--pname", dest="pname", default="none", help="Platform Name")
parser.add_argument('-s', "--short", dest="short", default="none", help="Release Short Description")

args = parser.parse_args()


def retrieve_json_object(file_path):
    # Opening JSON file
    f = open(file_path)

    with open(file_path, "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    return data


def write_json_file(obj, file):
    with open(file, "w") as jsonFile:
        json.dump(obj, jsonFile)
        jsonFile.close()
        return "Done"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    release = retrieve_json_object('devops/default_release.json')
    print(release)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
