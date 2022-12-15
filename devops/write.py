import json

from devops.retrieve import retrieve_json_object


def write_json_file(obj, file):
    with open(file, "w") as jsonFile:
        json.dump(obj, jsonFile)
        jsonFile.close()
    return "Done"


def write_release_manifest(release_manifest, archive, file_path):
    json_obj = json.loads(archive)
    json_obj.append(release_manifest)
    with open(file_path, "w") as jsonFile:
        json.dump(json_obj, jsonFile)
        jsonFile.close()
    return "Done"


def write_release_job(release, release_manifest, release_archive, develop_archive, develop_path, release_path):
    if release['createRelease']:
        write_release_manifest(release_manifest, release_archive, release_path)
    else:
        write_release_manifest(release_manifest, develop_archive, develop_path)

    reset_release = retrieve_json_object('devops/default_release.json')
    write_json_file(reset_release, 'release.json')
    return "Done"
