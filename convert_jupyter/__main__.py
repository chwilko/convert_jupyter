import getopt
import os
import sys

from . import clean, clean_all, jupyter2py, py2jupyter


def get_project_version() -> str:
    """Get project version from pyproject.toml [project] statment.

    Raises:
        EOFError: If pyproject.toml have not valid field.

    Returns:
        str: project version.
    """
    main_folder = sys.argv[0].split(os.sep)[:-2]
    with open(
        os.sep.join([*main_folder, "pyproject.toml"]), "r", encoding="utf-8"
    ) as toml:
        for line in toml:
            if line.strip() == "[project]":
                break
        for line in toml:
            if line.strip()[:7] == "version":
                return line.split("=", 1)[1].strip().replace("'", "").replace('"', "")
    raise EOFError("End of file.")


def safety_get_project_version() -> str:
    """Get project version, but if something work bad return empty string.

    Returns:
        str: project version or empty string.
    """
    try:
        version = get_project_version()
        return f" version {version}"
    except:  # pylint: disable=W0702 # noqa
        return ""


help_info = f"""convert_jupyter package{safety_get_project_version()}.
Usage:
  python3 -m convert_jupyter [options] <command> <input_file>

commands:
  jupyter2py                Convert jupyter file to python file.
  py2jupyter                Convert python file to jupyter file.
  clean                     Clean set jupyter file outputs.
  clean_all                 Clean all jupyter files outputs from the set folder and child folders

input_file -- name of input file to convert or clean.

General options:
  -o, --output              Set the output file name. By default, it is the input file name with a valid extension.
  -i, --input               Set input file directly.
  -c, --command             Set command directly.
  -f, --force               If file with output name exists overwrite them. By default raise error.
  -h, --help                Show help and exit.
  -V, --version             Show version and exit.
"""

short_help_info = """Usage:
  python3 -m convert_jupyter -o file_out --force command file
for more information type:
  python3 -m convert_jupyter --help
"""

force = False
out_file = None

try:
    opts, args = getopt.getopt(
        sys.argv[1:],
        "hVfo:i:c:",
        ["help", "version", "force", "=output", "=input", "=command"],
    )
except getopt.GetoptError:
    print(short_help_info)
    sys.exit(2)
print(opts, args)

command, in_file = None, None

for opt, arg in opts:
    if opt in ("-f", "--force"):
        force = True
    elif opt in ("-o", "--output"):
        out_file = arg
    elif opt in ("-i", "--input"):
        in_file = arg
    elif opt in ("-c", "--command"):
        command = arg
    elif opt in ("-h", "--help"):
        print(help_info)
        sys.exit(2)
    elif opt in ("-V", "--version"):
        print(get_project_version())
        sys.exit(2)

if command is None:
    if in_file is None:
        in_file = args[1]
    command = args[0]
else:
    if in_file is None:
        in_file = args[0]


command, in_file = args


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
