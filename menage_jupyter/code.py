import json

from convert_jupyter.constans import CEIL_SEPARATOR, MARKDOWN_BEGIN, MARKDOWN_END
f = open("out.txt", "w")

def decode(f_in_name: str, f_out_name: str = None):
    f_in = open(f_in_name, "r")
    if f_out_name is None:
        f_out_name = f_in_name.replace(".ipynb", ".py")
    f_out = open(f_out_name, "w")

    my_file = json.load(f_in)

    for cell in my_file["cells"]:
        print(CEIL_SEPARATOR, file = f_out)
        if cell["cell_type"] == "code":
            print(*cell["source"], sep = "", file = f_out)
        elif cell["cell_type"] == "markdown":
            print(MARKDOWN_BEGIN, *cell["source"], MARKDOWN_END, sep = "", file = f_out)


def get_markdown(value: str):
    value.replace(MARKDOWN_BEGIN, "")
    value.replace(MARKDOWN_END, "")

    cell = {
        "cell_type": "markdown",
        "source": value[len(MARKDOWN_BEGIN) + 1: -len(MARKDOWN_END)],
        "metadata": {},
    }
    return cell

def get_code(value: str):

    cell = {
        "cell_type": "code",
        "source": value,
        "metadata": {},
        "outputs": [],
    }
    return cell


def encode(f_in_name: str, f_out_name: str = None):

    f_in = open(f_in_name, "r")
    if f_out_name is None:
        f_out_name = f_in_name.replace(".py", ".ipynb")
    f_out = open(f_out_name, "w")
    ret = {}
    text = f_in.read()
    cells_text = text.split(CEIL_SEPARATOR)
    cells = []
    for cell in cells_text[1:]:
        cell = cell[1:]
        if cell[:len(MARKDOWN_BEGIN)] == MARKDOWN_BEGIN:
            cells.append(get_markdown(cell))
        else:
            cells.append(get_code(cell))
    ret["cells"] = cells
    
    ret["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3.8.10 64-bit",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.8.10"
        },
        "orig_nbformat": 4,
        "vscode": {
            "interpreter": {
                "hash": "916dbcbb3f70747c44a77c7bcd40155683ae19c65e1c03b4aa3499c5328201f1"
            }
        }
    },
    ret["nbformat"] = 4,
    ret["nbformat_minor"] = 2
    print(json.dumps(ret, indent=4), file = f_out)
