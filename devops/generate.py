from devops.defaults import staticReleaseValues
from devops.retrieve import retrieve_last_service_version, retrieve_major_value, retrieve_minor_value, \
    retrieve_revision_value
import datetime

def generate_release(release_json, generated_values):
    return release_json


def generate_service_version(release_json, archive):
    if len(archive) == 0:
        return "1.0.0"
    if release_json['breakingChanges']:
        last_release_version = retrieve_last_service_version(archive)
        retrieve_major_value(last_release_version)
        return str(int(retrieve_major_value(last_release_version)) + 1) + ".0.0"
    elif release_json['isRevision']:
        last_release_version = retrieve_last_service_version(archive)
        major_value = retrieve_major_value(last_release_version)
        minor_value = retrieve_minor_value(last_release_version)
        revision_value = retrieve_revision_value(last_release_version)
        return str(major_value) + "." + str(minor_value) + "." + str(int(revision_value) + 1)
    else:
        last_release_version = retrieve_last_service_version(archive)
        major_value = retrieve_major_value(last_release_version)
        minor_value = retrieve_minor_value(last_release_version)
        return str(major_value) + "." + str(int(minor_value) + 1) + ".0"


def generate_release_type(release_json):
    if release_json['breakingChanges']:
        return "major"
    elif release_json['isRevision']:
        return "revision"
    else:
        return "minor"


def generate_release(release_json, external_values, archive):

    tag = {True:  generate_service_version(release_json, archive), False:  datetime.datetime.now().strftime("%Y%m%d%H%M%S")} [release_json['createRelease']]
    release_manifest = {
        "platformName": external_values['platformName'],
        "serviceName": external_values['serviceName'],
        "serviceVersion": generate_service_version(release_json, archive),
        "releaseType": generate_release_type(release_json),
        "timestamp":    datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        "triggerMajor": release_json['breakingChanges'],
        "changeLogId": release_json['changeLogId'],
        "shortDescription": release_json['shortDescription'],
        "imageName": external_values['imageName'],
        "imageTag": tag,
        "deprecationCount": release_json['deprecationCount'],
        "exitCount": release_json['exitCount']
    }
    return release_manifest


