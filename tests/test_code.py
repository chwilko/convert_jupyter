from menage_jupyter.code import decode, encode


def test_decode():
    decode("scripts/reaserch/try.ipynb")

def test_encode():
    encode("scripts/reaserch/try.py", "scripts/reaserch/try2.ipynb")