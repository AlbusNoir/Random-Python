"""Lazy ezpz way to start new project"""
import os
import sys


def main():
    print('Lazy project generator')
    n = input('Enter name of project: ')

    confirm = input(f'Current directory is: {os.getcwd()}. Is this where you want the project?(yN): ')

    if confirm.lower() == 'y':
        print(f'Making project in {os.getcwd()}\\{n}')
        projdir = os.getcwd()+f'\\{n}'
    elif confirm.lower() == 'n':
        getdir = input(f'Current directory: {os.getcwd()}\nEnter directory for project: ')
        print(f'Making project in {getdir}\\{n}')
        projdir = f'{getdir}\\{n}'

        os.chdir(getdir)

    
    setup_proj(n, projdir)


def setup_proj(projectname, projectdir):
    projname = projectname
    projdir = projectdir

    print(os.getcwd())

    if os.path.exists(projdir):
        print(f'Cannot create {projname} in {os.getcwd()} because it already exists')
        rep = input('Would you like to try again?(yN): ')
        if rep.lower() == 'y':
            main()
        else:
            print('Okay then. Have a good one.')
            sys.exit(0)
    else:
        os.makedirs(projdir)
        os.chdir(projdir)
        venv_needed = input('Do you need a virtual environment?(yN): ')
        if venv_needed.lower() == 'y':
            venv_name = input('Name of virtual environment (if blank it will be "venv"): ')
            if venv_name:
                os.popen(f'python -m venv {venv_name}')
            else:
                os.popen('python -m venv venv')
    
    opennow = input('Do you want to open your new project now?(yN): ')
    if opennow.lower() == 'y':
        os.popen(f'code {projdir}')
    else:
        print('Okay then. Have a good one.')
        sys.exit(0)



if __name__ == '__main__':
    main()



