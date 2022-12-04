import os

from menage_jupyter.clean import clean


def test_clear():
    prefix = ["tests", "code"]
    TEST_FILE = os.sep.join(prefix + ["test_jupyter.ipynb"])
    TEST_FILE_CLEAR = os.sep.join(prefix + ["test_jupyter_clean.ipynb"])

    tmp_file = os.sep.join(prefix + ["tmp.ipynb"])
    with open(TEST_FILE, "r") as f_out:
        with open(tmp_file, "w") as f_in:
            f_in.write(f_out.read())
    clean(tmp_file)
    with open(TEST_FILE_CLEAR, "r") as f_expected:
        with open(tmp_file, "r") as f_actual:
            assert f_expected.read() == f_actual.read()
