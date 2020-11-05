import gitlab
from export import get_project_type

#Constants
OLD_GITLAB = 'http://gitlab.cloudlet-dev.com'
OLD_GITLAB_TOKEN = 'Ends with DI'


# Connect to GitLab API
gl = gitlab.Gitlab(OLD_GITLAB, OLD_GITLAB_TOKEN, per_page=1000 )
gl.auth()

count = 0

# Testing mistakes in determining project's types
def main():
    projects = gl.projects.list()

    for project in projects:
        print(f'project name is: {project.name}')
        ptype = get_project_type(project)
        print(f'type of project is: {ptype}')
        print()
        print()


if __name__ == '__main__':
    main()
