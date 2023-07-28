import json
import os
from typing import Any, Dict, List


def get_files_ext(path: str, ext: str = "ipynb") -> List[str]:
    """
    Function looks for files with the specified
    extension in the path and children's folders.

    Args:
        path (str): root
        ext (str, optional): extension searched for. Defaults to "ipynb".

    Returns:
        List[str]: list of files
    """
    ext_files = []
    for (root, _, files) in os.walk(path):
        for f in files:
            if f.split(".")[-1] == ext:
                ext_files.append(os.sep.join([root, f]))
    return ext_files


def clean_all(path: str) -> None:
    """The function recursively finds all jupyter files
        and clears their output.

    Args:
        path (str): path with files to clean
    """
    files_to_clear = get_files_ext(path, ext="ipynb")
    for f in files_to_clear:
        clean(f)


def clean(path: str) -> None:
    """Function clean jupyter file output.

    Args:
        path (str): file to cleancells
    """
    with open(path, "r", encoding="utf-8") as f:
        my_file = json.load(f)
    new_cells = []
    for cell in my_file["cells"]:
        new_cell: Dict[str, Any] = {}
        if cell["cell_type"] == "code":
            new_cell["outputs"] = []
            new_cell["execution_count"] = None
        for key in ("cell_type", "metadata", "source"):
            new_cell[key] = cell[key]
        new_cells.append(new_cell)
    my_file["cells"] = new_cells
    with open(path, "w", encoding="utf-8") as f:
        print(json.dumps(my_file, indent=1, sort_keys=True), file=f)


if __name__ == "__main__":
    file_to_clear = get_files_ext(os.getcwd())[0]
    print(file_to_clear)
    clean(file_to_clear)
