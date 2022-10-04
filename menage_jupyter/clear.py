import json
import os


def get_files_ext(path: str, ext: str="ipynb"):
    ext_files = []
    for (root, _, files) in os.walk(path):#, topdown=True):
        for f in files:
            if f.split(".")[-1] == ext:
                ext_files.append(os.sep.join([root, f]))
    return ext_files


def clear(path: str):
    with open(path, "r") as f:
        my_file = json.load(f)
    new_cells = []
    for cell in my_file["cells"]:
        new_cell = {}
        for key in ("cell_type", "metadata", "source"):
            new_cell[key] = cell[key]
        new_cells.append(new_cell)
    my_file["cells"] = new_cells
    with open(path, "w") as f:
        print(json.dumps(my_file, indent=4), file = f)


if __name__ == "__main__":
    file_to_clear = get_files_ext(os.getcwd())[0]
    print(file_to_clear)
    clear(file_to_clear)