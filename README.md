# Convert jupyter 
This project help convert jupyter flie.
It let:
    - convert .ipynb to .py file
    - convert .py to .ipynb file
    - clean output jupyter


## autors
Bartłomiej Chwiłkowski (github: chwilko)


# Structure
convert_jupyter:
    - file with functions


## Functions 

jupyter2py(f_in_name: str, f_out_name: str = None)

py2jupyter(f_in_name: str, f_out_name: str = None)

clean(path: str)
    Function clean jupyter file output.

clean_all(path: str)
    The function recursively finds all jupyter files and clears their output.


## Licence
MIT