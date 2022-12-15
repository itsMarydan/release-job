import argparse
import datetime
import json


# Function to Retrieve single Json Object from Json File

def retrieve_json_object(file_path):
    # Open and load JSON file
    with open(file_path, "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    return data


# Function to Retrieve multiple Json Objects from Json File as array

def retrieve_json_objects(file_path):
    # Opening JSON file
    with open(file_path, "r") as jsonFile:
        data = json.load(jsonFile)
        data = json.dumps(data)
        jsonFile.close()
    return data


def retrieve_last_release(archive):
    json_obj = json.loads(archive)
    return json_obj[-1]


def retrieve_last_service_version(archive):
    json_obj = json.loads(archive)
    return json_obj[-1]['serviceVersion']


def retrieve_major_value(version):
    return version.split('.')[0]


def retrieve_minor_value(version):
    return version.split('.')[1]


def retrieve_revision_value(version):
    return version.split('.')[2]
