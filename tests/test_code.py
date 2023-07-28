import pytest

from convert_jupyter.code import jupyter2py, py2jupyter


def test_decode():
    jupyter2py("tests/code/try.ipynb", "tests/code/tmp.py", force=True)
    with open("tests/code/tmp.py", "r") as expected, open(
        "tests/code/try3.py", "r", encoding="utf-8"
    ) as actual:
        assert expected.read() == actual.read()


def test_encode():
    py2jupyter("tests/code/try.py", "tests/code/tmp.ipynb", force=True)
    with open("tests/code/tmp.ipynb", "r") as expected, open(
        "tests/code/try3.ipynb", "r", encoding="utf-8"
    ) as actual:
        assert expected.read() == actual.read()


def test_reverse_code():
    py2jupyter("tests/code/try.py", "tests/code/tmp.ipynb", force=True)
    jupyter2py("tests/code/tmp.ipynb", "tests/code/try3.py", force=True)
    with open("tests/code/try.py", encoding="utf-8") as begin, open(
        "tests/code/try3.py", encoding="utf-8"
    ) as end:
        assert begin.read() == end.read()


def test_errors():
    with pytest.raises(FileExistsError):
        py2jupyter("tests/code/try.py", "tests/code/try3.ipynb")

    with pytest.raises(FileExistsError):
        jupyter2py("tests/code/try3.ipynb", "tests/code/try3.py")
