import pytest

from menage_jupyter.code import jupyter2py, py2jupyter


def test_decode():
    jupyter2py("tests/code/try.ipynb", "tests/code/try3.py", force=True)
    with open("tests/code/try.py", "r") as expected, open(
        "tests/code/try3.py", "r"
    ) as actual:
        assert expected.read() == actual.read()


def test_reverse_code():
    py2jupyter("tests/code/try.py", "tests/code/try3.ipynb", force=True)
    jupyter2py("tests/code/try3.ipynb", "tests/code/try3.py", force=True)
    with open("tests/code/try.py") as begin, open("tests/code/try3.py") as end:
        assert begin.read() == end.read()


def test_errors():
    with pytest.raises(FileExistsError):
        py2jupyter("tests/code/try.py", "tests/code/try3.ipynb")

    with pytest.raises(FileExistsError):
        jupyter2py("tests/code/try3.ipynb", "tests/code/try3.py")
