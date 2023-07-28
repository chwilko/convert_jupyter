import getopt
import sys

from . import clean, clean_all, jupyter2py, py2jupyter

force = False
out_file = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "o:f:", ["force"])
except getopt.GetoptError:
    print("Usage: python3 -m convert_jupyter", "-o file_out --force 1 command file")
    sys.exit(2)

command, in_file = args

for opt, arg in opts:
    if opt == "--force":
        force = bool(arg)
    elif opt == "-f":
        force = bool(arg)
    elif opt == "-o":
        out_file = arg


if out_file is None:
    out_file = ".".join([*in_file.split(".")[:-1], "ipynb"])

if command == "jupyter2py":
    jupyter2py(in_file, out_file, force)
elif command == "py2jupyter":
    py2jupyter(in_file, out_file, force)
elif command == "clean":
    clean(in_file)
elif command == "clean_all":
    clean_all(in_file)
else:
    raise ValueError(
        "command have to be from", '{"py2jupyter", "jupyter2py", "clean", "clean_all"}'
    )
