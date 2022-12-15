### Release Job

This is a simple job that will run on every push to the master branch. It will build the project and create a release manifest.


#### PARAMETERS

* `service` - The name of your microservice, set this value using the -s or --service flag.
* `platform version` - The version of your platform, set this value using the -pv or --pversion flag.
* `platform name` - The name of your platform, set this value using the -pn or --pname flag.
* `image` - The name of your image, set this value using the -i or --image flag.
* `help` - Show help, set this value using the -h or --help flag.

#### Developer Notes

* This job will run on every push to the master branch.
* This job will build the project and create a release manifest.
* To use this job correctly, you must set the release.json file with the correct data before creating a pull request
* The release.json file is located in the root of the project.

#### What is in the release.json file?
```json
{
  "createRelease": false,
  "breakingChanges": false,
  "changeLogId": 6789,
  "isRevision": false,
  "shortDescription": "Enter A Short Description",
  "blame": "itsMaryDan",
  "deprecationCount": 1,
  "exitCount": 1
}
```

* `createRelease` - Set this value to true if you want to create a release.
* `breakingChanges` - Set this value to true if you have breaking changes.
* `changeLogId` - Set this value to the change log id for reference.
* `isRevision` - Set this value to true if you are creating a revision.
* `shortDescription` - Set this value to a short description of the release.
* `blame` - Set this value to the person who is responsible for the release.
* `deprecationCount` - Set this value to the number of api deprecations.
* `exitCount` - Set this value to the number of api exits.

 **WARNING**: After each run, the release.json file will reset to the default.

To include this into your project, add the following to your .git-actions-ci.yml file:

```yaml
name: Resources
on: repository_dispatch
jobs:
    resources:
        name: Update resources
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v1

            - uses: actions/setup-python@v4
              with:
                  python-version: 3.8
                  
            - uses: actions/checkout@v3
              with:
                fetch-depth: 2
            - run: git checkout HEAD^     

            - name: Generate Release Manifest
              run:  python3 main.py -s $SERVICE_NAME -i $IMAGE_NAME -pv $PLATFORM_VERSION -pn $PLATFORM_NAME 

            - name: Update Repository
              uses: test-room-7/action-update-file@v1
              with:
                  commit-msg: Update resources
                  github-token: ${{ secrets.GITHUB_TOKEN }}
    
```

### Build Job Test 

To test the build job, you can use the following command t:

```bash
 python main.py -s sagas -pv 5.2.0 -i equilizer/sagas -pn equilizer 
```