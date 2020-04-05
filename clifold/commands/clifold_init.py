"""Setup file for python project."""
import os
import requests


def py_init(init, project_path, pname):
    '''
    Setup file creation function.

    Args:
        init: True or False
        project_path: initialize setup.py in project directory

    Returns:
        Initialize successful or not
    '''
    if init:
        # Create README and MANIFEST file
        os.chdir(project_path)
        open('README.md', 'w').close()

        with open('MANIFEST.in', 'w') as mani:
            mani.write('include *.md')
            mani.close()
        print("\n📄 Created README.md & MANIFEST.in ...")

        # fetch .gitignore
        gitig = requests.get(
            'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore')
        with open('.gitignore', 'wb') as gig:
            for chunk in gitig.iter_content():
                gig.write(chunk)
            gig.close()
        print("\n🚀 Fetched .gitignore from GitHub...")

        # fetch setup.py from PyPa
        setup = requests.get(
            'https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py')
        with open('setup.py', 'wb') as s:
            for chunk in setup.iter_content():
                s.write(chunk)
            s.close()
        print("\n✨ Requested setup.py...")
        return 1
    else:
        print("\nNo setup.py created...")
        return 0
