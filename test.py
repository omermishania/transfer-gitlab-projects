import gitlab
from export import get_project_type

# Connect to GitLab API
gl = gitlab.Gitlab('http://gitlab.cloudlet-dev.com', private_token='yxmHENWaJuz1dzCjydDi', per_page=1000 )
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
