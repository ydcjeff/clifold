"""Main file for clifold."""
import argparse

from clifold.commands.clifold_git import git_init
from clifold.commands.clifold_init import py_init
from clifold.commands.clifold_pkg import pip
from clifold.commands.clifold_project import create


def __version__():
    """return package version"""
    return "0.2.8"


def cli():
    """CLI parsing"""
    parser = argparse.ArgumentParser(
        prog='clif',
        usage='%(prog)s <arg> [options]',
        description='🚀 A CLI tool for scaffolding any Python Projects 🚀',
        conflict_handler='resolve')

    group = parser.add_argument_group('Argument')
    group.add_argument('project_name', help='Project name to create with venv')

    group = parser.add_argument_group('Options')
    group.add_argument('-g', '--git', action='store_true', default=True,
                       dest='git', help='Make git initialization')
    group.add_argument('-ng', '--no-git', action='store_false',
                       dest='git', help='Skip git initialization')

    group.add_argument('-p', '--pkg', action='store_true', default=True,
                       dest='pkg', help='Ask packages to install')
    group.add_argument('-np', '--no-pkg', action='store_false', dest='pkg',
                       help='Skip packages installation')

    group.add_argument('-i', '--init', action='store_true', default=True,
                       dest='init', help='Create setup.py file')
    group.add_argument('-ni', '--no-init', action='store_false',
                       dest='init', help='Skip setup.py file')

    group.add_argument('-V', '--version', action='version',
                       version=__version__(), help='Output version number')
    group.add_argument('-h', '--help', action='help',
                       help='Output usage information')

    args = parser.parse_args()
    pname = args.project_name
    git = args.git
    pkg = args.pkg
    init = args.init

    ppath, root = create(pname)
    git_init(git, ppath)
    pip(pkg, root, pname)
    py_init(init, ppath, pname)


if __name__ == "__main__":
    cli()
