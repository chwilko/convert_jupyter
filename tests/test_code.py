from menage_jupyter.code import jupyter2py, py2jupyter


def test_decode():
    jupyter2py("scripts/reaserch/try.ipynb", "scripts/reaserch/try3.py")
    with open("scripts/reaserch/try2.py") as expected, open("scripts/reaserch/try3.py") as actual:
        assert expected.read() == actual.read()


def test_encode():
    py2jupyter("scripts/reaserch/try.py", "scripts/reaserch/try3.ipynb")
    with open("scripts/reaserch/try2.ipynb") as expected, open("scripts/reaserch/try3.ipynb") as actual:
        assert expected.read() == actual.read()
    
def reverse_code1():
    py2jupyter("scripts/reaserch/try.py", "scripts/reaserch/try3.ipynb")
    jupyter2py("scripts/reaserch/try3.ipynb", "scripts/reaserch/try3.py")
    with open("scripts/reaserch/try.py") as begin, open("scripts/reaserch/try3.py") as end:
        assert begin.read() == end.read()

def reverse_code2():
    jupyter2py("scripts/reaserch/try.ipynb", "scripts/reaserch/try3.py")
    py2jupyter("scripts/reaserch/try3.py", "scripts/reaserch/try3.ipynb")
    with open("scripts/reaserch/try.ipynb") as begin, open("scripts/reaserch/try3.ipynb") as end:
        assert begin.read() == end.read()