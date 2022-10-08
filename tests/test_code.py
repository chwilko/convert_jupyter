from menage_jupyter.code import jupyter2py, py2jupyter


def test_decode():
    jupyter2py("scripts/reaserch/try.ipynb")


def test_encode():
    py2jupyter("scripts/reaserch/try.py", "scripts/reaserch/try2.ipynb")
