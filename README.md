

# Transferring Gitlab Projects from/to Gitlab


## *** IMPORTANT NOTES ***

 1. Please make sure you change the `PATH` constant **in both scripts** to the location you've download this project.
 2. Please make sure you change the `OLD_GITLAB` and `NEW_GITLAB`  constants **in both scripts** to your desired addresses.
 3. Please run the import.py script **only after** you are sure that the export.py script run successfully and all the projects are placed in the correct folder.

## Files Description

| File | Description |
|--|--|
| `export.py` | This script is used to export Gitlab projects from the old Gitlab.cloudlet-dev.com to local files in your PC. |
| `import.py` | This script is used to import Gitlab projects from local files in your PC to the new Gitlab.com Group. |
| `test.py` | This script is used to test the division of the projects to subgroups on the new Gitlab.com Group. |


## Configuring the constants
The following table lists the configurable constants. Configure them to your desired purposes.

| Parameter         | Description              | Default                              |
| ------------------| -------------------------| -------------------------------------|
| `PATH`            | Path of the downloaded repo                                  | `'C:\\Users\\Computer\\Desktop\\import-to-gitlab'` |
| `OLD_GITLAB`      | Gitlab address of the projects you would like to **export**  | `'http://gitlab.cloudlet-dev.com'` |
| `OLD_GITLAB_TOKEN`| Private token of the old Gitlab address                      | `'Ends with DI'`  |
| `SUBGROUPS`       | List of subgroups to divide the projects                     | `['helms', 'unknown', 'ansible', 'applications']`      |
| `NEW_GITLAB`      | Gitlab address of the projects you would like to **import**  | `'https://gitlab.com'`     |
| `NEW_GITLAB_TOKEN`| Private token of the new Gitlab address                      | `'Ends with SO'`  |
| `SUBGROUPS_DICT`       | Dictionary of the new GItlab subgroups and their ID's                 | `{'helms': '9032559', 'applications': '9032575', 'ansible': '9032553', 'unknown': '9142157'}`    |


