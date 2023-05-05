import os


def test_decode():
    os.system(
        "python3 -m menage_jupyter -f 1 -o tests/code/tmp.py jupyter2py tests/code/try.ipynb"
    )
    with open("tests/code/tmp.py", "r") as expected, open(
        "tests/code/try3.py", "r"
    ) as actual:
        assert expected.read() == actual.read()


def test_encode():
    os.system(
        "python3 -m menage_jupyter -f 1 -o tests/code/tmp.ipynb py2jupyter tests/code/try.py"
    )
    with open("tests/code/tmp.ipynb", "r") as expected, open(
        "tests/code/try3.ipynb", "r"
    ) as actual:
        assert expected.read() == actual.read()


def test_reverse_code():
    os.system(
        "python3 -m menage_jupyter -f 1 -o tests/code/tmp.ipynb py2jupyter tests/code/try.py"
    )
    os.system(
        "python3 -m menage_jupyter -f 1 -o tests/code/tmp.py jupyter2py tests/code/tmp.ipynb"
    )
    with open("tests/code/try.py") as begin, open("tests/code/tmp.py") as end:
        assert begin.read() == end.read()


def test_errors():
    assert 256 == os.system(
        "python3 -m menage_jupyter -o tests/code/tmp.ipynb py2jupyter tests/code/try.py"
    )
    assert 256 == os.system(
        "python3 -m menage_jupyter -o tests/code/tmp.py jupyter2py tests/code/try.ipynb"
    )
