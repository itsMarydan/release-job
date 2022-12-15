import argparse
import datetime
import json

from devops.generate import generate_service_version, generate_release_type, generate_release
from devops.retrieve import retrieve_json_object, retrieve_json_objects
from devops.write import write_release_manifest, write_release_job

parser = argparse.ArgumentParser()

x = datetime.datetime.now()

default_tag = x.strftime("%Y%m%d%H%M%S")
default_type = "minor"
timestamp = x

parser.add_argument('-s', "--service", dest="service", default="default", help="Service Name")
parser.add_argument('-pv', "--pversion", dest="pversion", default="default", help="Platform Version")
parser.add_argument('-i', "--image", dest="image", default="default", help="Image Name")
parser.add_argument('-pn', "--pname", dest="pname", default="default", help="Platform Name")


args = parser.parse_args()

external_values = {
    "platformName": args.pname,
    "serviceName": args.service,
    "platformVersion": args.pversion,
    "imageName": args.image,
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    release = retrieve_json_object('release.json')
    release_archive = retrieve_json_objects('devops/release_archive.json')
    develop_archive = retrieve_json_objects('devops/develop_archive.json')
    manifest = generate_release(release, external_values, release_archive)
    print("Write the release manifest to a file")
    write_release_job(release, manifest, release_archive, develop_archive, 'devops/develop.json', 'devops/release.json')
    print("Done")




