# Convert jupyter 
This project help convert jupyter flie.
It let:
    - convert .ipynb to .py file
    - convert .py to .ipynb file
    - clean output jupyter


## autors
Bartłomiej Chwiłkowski (github: chwilko)


# Usage:
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


# Structure
convert_jupyter:
    - file with functions

tests:
    - tests


## Functions 

jupyter2py(
    f_in_name: str,
    f_out_name: Union[str, None] = None,
    force: bool = False
)
    Convert jupyter file f_in_name to python file f_out_name.

py2jupyter(f_in_name: str, f_out_name: str = None)
    Convert python file f_in_name to jupyter file f_out_name.

clean(path: str)
    Function clean jupyter file output.

clean_all(path: str)
    The function recursively finds all jupyter files and clears their output.


## Licence
MIT