"""Checking the output of test_commands.py"""
import os


def test_check():
    os.system("cd ..")
    output1 = os.path.exists("testing-venv")
    output2 = os.path.exists("testing-venv/bin")
    output3 = os.path.exists("testing-venv/include")
    output4 = os.path.exists("testing-venv/lib")
    output5 = os.path.exists("testing-venv/pyvenv.cfg")
    output6 = os.path.exists("testing-venv/testing")
    output7 = os.path.exists("testing-venv/testing/testing")
    output8 = os.path.exists("testing-venv/testing/testing/__init__.py")
    output9 = os.path.exists("testing-venv/testing/testing/main.py")
    output10 = os.path.exists("testing-venv/testing/tests")
    output11 = os.path.exists("testing-venv/testing/tests/__init__.py")
    output12 = os.path.exists("testing-venv/testing/tests/test_main.py")
    output13 = os.path.exists("testing-venv/testing/.gitignore")
    output14 = os.path.exists("testing-venv/testing/MANIFEST.in")
    output15 = os.path.exists("testing-venv/testing/README.md")
    output16 = os.path.exists("testing-venv/testing/setup.py")

    assert output1 == True
    assert output2 == True
    assert output3 == True
    assert output4 == True
    assert output5 == True
    assert output6 == True
    assert output7 == True
    assert output8 == True
    assert output9 == True
    assert output10 == True
    assert output11 == True
    assert output12 == True
    assert output13 == True
    assert output14 == True
    assert output15 == True
    assert output16 == True
