import gitlab
import re
import time
import os

# Constants
PATH = 'C:\\Users\\Computer\\Desktop\\import-to-gitlab'
SUBGROUPS = ['helms', 'unknown', 'ansible', 'applications']

# Determines the type of the project
def get_project_type(project):
    files = project.repository_tree()

    for file in files:
        filename = (file.get('name'))
        print(filename)

        if filename == 'Chart.yaml':
            project_type = 'helms'
            break

        elif filename.endswith('.py'):
            project_type = 'applications'
            break

        if filename == 'roles':
            project_type = 'ansible'
            break

        else:
            project_type = 'unknown'
    return project_type


def directories_setup():
    for subgroup in SUBGROUPS:
        if not os.path.exists(f'{PATH}//{subgroup}'):
            os.makedirs(f'{PATH}//{subgroup}')


def main():
    directories_setup()
    # Connect to GitLab API
    gl = gitlab.Gitlab('http://gitlab.cloudlet-dev.com', private_token='yxmHENWaJuz1dzCjydDi', per_page=1000)
    gl.auth()

    # Total downloaded projects
    count = 0

    projects = gl.projects.list()
    for project in projects:

        # Work only on role repositories
        if not re.match(r'^role', project.name):
            print(f'Exporting project: {project.name}...')
            count += 1

            # Create the export
            p = gl.projects.get(project.id)
            export = p.exports.create()

            # Wait for the 'finished' status
            export.refresh()
            while export.export_status != 'finished':
                time.sleep(1)
                export.refresh()

            # Get the subgroup of the project
            sgroup = get_project_type(project)

            # Download the result
            with open(f'{PATH}\\{sgroup}\\{project.name}.tgz', 'wb') as file:
                export.download(streamed=True, action=file.write)
                print(f'type of project is: {sgroup}')
                print(f'project: {project.name} Downloaded successfully')
                print()
                print()
                print()
    print(f'{count} projects downloaded successfully')


if __name__ == '__main__':
    main()
