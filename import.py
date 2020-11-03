import gitlab
import time
import glob
import os

# Constants
PATH = 'C:\\Users\\Computer\\Desktop\\import-to-gitlab'


def main():
    # Dict with project types and subgroups id's
    subgroups = {'helms': '9032559', 'applications': '9032575', 'ansible': '9032553', 'unknown': '9142157'}
    subgroup_directories = ['helms', 'unknown', 'ansible', 'applications']

    # Connect to GitLab API
    gl = gitlab.Gitlab('https://gitlab.com', private_token='kDTxtmkoVxFoJXPz3sso', per_page=1000)

    for subgroup_directory in subgroup_directories:
        # Create List of all the exported files
        os.chdir(f"{PATH}\\{subgroup_directory}")
        project_files = glob.glob("*")

        for project_file in project_files:
            print(f'importing project: {project_file}...')

            # Set project name
            project_name = project_file.split('.')[0].replace(' ', '-')
            print(project_name)

            # If file doesn't exist, import it
            try:
                # Opens exported file
                output = gl.projects.import_project(open(project_file, 'rb'), namespace=subgroups[subgroup_directory], path=project_name)

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
