"""Git initialization in project folder."""
import os
import shutil
import subprocess


def git_init(git, project_path):
    '''
    Git initialization function.

    Args:
        git: True or False
        project_path: absolute path to the project

    Returns:
        print Success or Error message
    '''
    if git:
        git_path = shutil.which('git')
        if os.path.exists(git_path):
            os.chdir(project_path)
            subprocess.run([git_path, 'init'], check=True)
        else:
            raise OSError("Git not found!")
        return 1
    else:
        print("Git not initialized...")
        return 0
