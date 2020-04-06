<p align="center"><a href="https://ydcjeff.github.io/clifold" target="_blank" rel="noopener noreferrer"><img width="100" src="https://ydcjeff.github.io/clifold/logo.png" alt="Clifold logo"></a></p>

<h2 align="center">Clifold</h2>

<p align="center">
  <a href="https://circleci.com/gh/ydcjeff/clifold"><img src="https://circleci.com/gh/ydcjeff/clifold.svg?style=svg"></a>
  <a href="https://github.com/ydcjeff/clifold/actions"><img src="https://github.com/ydcjeff/clifold/workflows/Python%20package/badge.svg?branch=master"></a>
  <a href="https://travis-ci.com/github/ydcjeff/clifold"><img src="https://travis-ci.com/ydcjeff/clifold.svg?branch=master"></a>
</p>


Clifold is a command line tool that can quickly scaffold the python projects.

## Requirements
- Minimum Python 3.6 installed
- Pip 3 installed

## Installation

First, make sure you have at least [python3.6](https://python.org) and [pip3](https://pypi.org/project/pip/) installed.

### Linux

In linux distributions, at least python3.6 is normally preinstalled, but pip3 isn't. To install pip3 and clifold in linux distributions,

#### Arch Linux
```
sudo pacman -S python-pip
pip3 install clifold
```
#### Debian/Ubuntu
```
sudo apt install python3-venv python3-pip
pip3 install clifold
```
#### openSUSE
```
sudo zypper install python3-pip python3-setuptools python3-wheel
pip3 install clifold
```
#### Fedora
```
sudo dnf install python3 python3-wheel
pip3 install clifold
```
#### CentOS/RHEL

For CentOS/RHEL, please follow [this link](https://packaging.python.org/guides/installing-using-linux-tools/#centos-rhel).

### macOS

Pip3 probably have been installed if python3 has been installed from python.org. After that,

```
pip3 install clifold
```

### Windows
```
pip3 install clifold
```

## Usage

After clifold has been installed, you will have `clif` command to start using.

```
usage: clif <arg> [options]

🚀 A CLI tool for scaffolding any Python Projects 🚀

Argument:
  project_name    Project name to create with venv

Options:
  -g, --git       Make git initialization (Default: True)
  -ng, --no-git   Skip git initialization
  -p, --pkg       Ask packages to install (Default: True)
  -np, --no-pkg   Skip packages installation
  -i, --init      Create setup.py file (Default: True)
  -ni, --no-init  Skip setup.py file
  -V, --version   Output version number
  -h, --help      Output usage information
```

[![asciicast](https://asciinema.org/a/317100.svg)](https://asciinema.org/a/317100)

## LICENSE

[MIT](https://opensource.org/licenses/MIT)