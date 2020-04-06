"""Testing various commands of clifold"""
import os
import pytest

from clifold import clifold_main


def test_as_module():
    exit_status = os.system('python3 -m clifold')
    assert exit_status == 256


def test_help():
    help_status = os.system('clif --help')
    h_status = os.system('clif -h')
    assert help_status == 0
    assert h_status == 0


def test_version():
    ver_status = os.system('clif --version')
    v_status = os.system('clif -V')
    assert ver_status == 0
    assert v_status == 0


def test_git():
    git_status = os.system('clif --git')
    g_status = os.system('clif -g')
    assert git_status == 512
    assert g_status == 512


def test_pkg():
    pkg_status = os.system('clif --pkg')
    p_status = os.system('clif -p')
    assert pkg_status == 512
    assert p_status == 512


def test_init():
    init_status = os.system('clif --init')
    i_status = os.system('clif -i')
    assert init_status == 512
    assert i_status == 512


def test_nogit():
    nogit_status = os.system('clif --no-git')
    ng_status = os.system('clif -ng')
    assert nogit_status == 512
    assert ng_status == 512


def test_nopkg():
    nopkg_status = os.system('clif --no-pkg')
    np_status = os.system('clif -np')
    assert nopkg_status == 512
    assert np_status == 512


def test_noinit():
    noinit_status = os.system('clif --no-init')
    ni_status = os.system('clif -ni')
    assert noinit_status == 512
    assert ni_status == 512


def test_proj():
    np_status = os.system('clif testing -g -np -i')
    ngnp_status = os.system('clif testing -ng -np -i')
    ngnpni_status = os.system('clif testing -ng -np -ni')
    assert np_status == 0
    assert ngnp_status == 0
    assert ngnpni_status == 0


def test_proje():
    np_status = os.system('clif testing -g -np -i')
    ngnp_status = os.system('clif testing -ng -np -i')
    ngnpni_status = os.system('clif testing -ng -np -ni')
    assert np_status == 0
    assert ngnp_status == 0
    assert ngnpni_status == 0


def test_project():
    np_status = os.system('clif testing --g --np --i')
    ngnp_status = os.system('clif testing --ng --np --i')
    ngnpni_status = os.system('clif testing --ng --np --ni')
    assert np_status == 512
    assert ngnp_status == 512
    assert ngnpni_status == 512


def test_arbitary_commands():
    arbitary_status = os.system('clif flaksjdfljasd --g -asd-fasd-f-dgsdf-adsf')
    assert arbitary_status == 512


def test_proj_only():
    output = os.system('clif torch')
    assert output == 256


def test_cli():
    with pytest.raises(SystemExit):
        clifold_main.cli()
        pytest.fail("CLI doesn't asking for a command argument...")
