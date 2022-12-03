from menage_jupyter.code import jupyter2py, py2jupyter


def test_decode():
    jupyter2py("tests/code/try.ipynb", "tests/code/try3.py")
    with open("tests/code/try.py", "r") as expected, open("tests/code/try3.py", "r") as actual:
        expected = expected.read()
        actual = actual.read()
        print(actual)
        print(expected)
        for i in range(len(expected)):
            print(i, expected[i], actual[i])
            # assert expected[i] == actual[i]
        # assert expected.read() == actual.read()



def test_reverse_code():
    py2jupyter("tests/code/try.py", "tests/code/try3.ipynb")
    jupyter2py("tests/code/try3.ipynb", "tests/code/try3.py")
    with open("tests/code/try.py") as begin, open("tests/code/try3.py") as end:
        assert begin.read() == end.read()


