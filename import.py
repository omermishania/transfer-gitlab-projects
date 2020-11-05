import gitlab
import time
import glob
import os

# Constants
PATH = 'C:\\Users\\Computer\\Desktop\\import-to-gitlab'
NEW_GITLAB = 'https://gitlab.com'
NEW_GITLAB_TOKEN = 'Ends with SO'
SUBGROUPS = ['helms', 'unknown', 'ansible', 'applications']
SUBGROUPS_DICT = {'helms': '9032559', 'applications': '9032575', 'ansible': '9032553', 'unknown': '9142157'}  # Dict with project types and subgroups id's


def main():
    # Connect to GitLab API
    gl = gitlab.Gitlab(NEW_GITLAB, NEW_GITLAB_TOKEN, per_page=1000)

    for subgroup in SUBGROUPS:
        # Create List of all the exported files
        os.chdir(f"{PATH}\\{subgroup}")
        project_files = glob.glob("*")

        for project_file in project_files:
            print(f'importing project: {project_file}...')

            # Set project name
            project_name = project_file.split('.')[0].replace(' ', '-')
            print(project_name)

            # If file doesn't exist, import it
            try:
                # Opens exported file
                output = gl.projects.import_project(open(project_file, 'rb'), namespace=SUBGROUPS_DICT[subgroup], path=project_name)

                # Get a ProjectImport object to track the import status
                project_import = gl.projects.get(output['id'], lazy=True).imports.get()

                # While import is not finished
                while project_import.import_status != 'finished':
                    time.sleep(1)
                    project_import.refresh()

                print(f'project: {project_name} imported successfully')

            # If file already exists, pass
            except gitlab.exceptions.GitlabHttpError as e:
                print(e)


if __name__ == '__main__':
    main()
