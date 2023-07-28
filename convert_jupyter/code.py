import json
from os.path import exists
from typing import Any, Dict, Union

from .constans import CELL_SEPARATOR, MARKDOWN_BEGIN, MARKDOWN_END


def jupyter2py(
    f_in_name: str,
    f_out_name: Union[str, None] = None,
    force: bool = False,
) -> None:
    """Function convert .ipynb to .py file.

    Function convert .ipynb to .py file.
    All cells after convert are separate to possible is revert convert.
    Markdown cells are commented.

    Args:
        f_in_name (str): File to convert name.
        f_out_name (str, optional): Converted file name.
            If None new file have the same name as old file,
            but other extenction. Defaults to None.
        force (bool, optional): If False if f_out_name file exists raise error.
            If True f_out_name is overwrite. Defaults to False.

    Raises:
        FileExistsError: If file should be overwritten, but force is False
    """
    if f_out_name is None:
        f_out_name = f_in_name.replace(".ipynb", ".py")
    if force is False and exists(f_out_name):
        raise FileExistsError(
            f"{f_out_name} exist, use force=True to overwrite",
        )
    with open(f_in_name, "r", encoding="utf-8") as f_in, open(
        f_out_name, "w", encoding="utf-8"
    ) as f_out:
        my_file = json.load(f_in)
        for i, cell in enumerate(my_file["cells"]):
            if i > 0:
                print(CELL_SEPARATOR, file=f_out, end="")
            if cell["cell_type"] == "code":
                print(*cell["source"], sep="", file=f_out, end="")
            elif cell["cell_type"] == "markdown":
                print(
                    MARKDOWN_BEGIN,
                    *cell["source"],
                    MARKDOWN_END,
                    sep="",
                    file=f_out,
                    end="",
                )


def py2jupyter(
    f_in_name: str,
    f_out_name: Union[str, None] = None,
    force: bool = False,
) -> None:
    """Function convert .py to .ipynb file.

    Function convert .py to .ipynb file.
    Cells separator is {CELL_SEPARATOR}.
    Markdown cells starts by {MARKDOWN_BEGIN} end end by {MARKDOWN_END}

    Args:
        f_in_name (str): File to convert name.
        f_out_name (str, optional): Converted file name.
            If None new file have the same name as old file,
            but other extenction. Defaults to None.
        force (bool, optional): If False if f_out_name file exists raise error.
            If True f_out_name is overwrite. Defaults to False.

    Raises:
        FileExistsError: If file should be overwritten, but force is False
    """
    if f_out_name is None:
        f_out_name = f_in_name.replace(".py", ".ipynb")
    if force is False and exists(f_out_name):
        raise FileExistsError(
            f"{f_out_name} exist, use force=True to overwrite",
        )

    with open(f_in_name, "r", encoding="utf-8") as f_in, open(
        f_out_name, "w", encoding="utf-8"
    ) as f_out:

        ret: Dict[str, Any] = {}
        text = f_in.read()
        cells_text = text.split(CELL_SEPARATOR)
        cells = []
        for cell in cells_text:
            if cell[: len(MARKDOWN_BEGIN)] == MARKDOWN_BEGIN:
                cells.append(_get_markdown(cell))
            else:
                cells.append(_get_code(cell))
        ret["cells"] = cells

        ret["metadata"] = (
            {
                "kernelspec": {
                    "display_name": "Python 3.8.10 64-bit",
                    "language": "python",
                    "name": "python3",
                },
                "language_info": {
                    "codemirror_mode": {"name": "ipython", "version": 3},
                    "file_extension": ".py",
                    "mimetype": "text/x-python",
                    "name": "python",
                    "nbconvert_exporter": "python",
                    "pygments_lexer": "ipython3",
                    "version": "3.8.10",
                },
                "orig_nbformat": 4,
                "vscode": {
                    "interpreter": {
                        "hash": (
                            "916dbcbb3f70747c44a77c7bcd40155683"
                            "ae19c65e1c03b4aa3499c5328201f1"
                        )
                    }
                },
            },
        )
        ret["nbformat"] = (4,)
        ret["nbformat_minor"] = 2
        print(json.dumps(ret, indent=4), file=f_out, end="")


def _get_markdown(value: str):
    cell = {
        "cell_type": "markdown",
        "source": value[len(MARKDOWN_BEGIN) : -len(MARKDOWN_END)],  # noqa
        "metadata": {},
    }
    return cell


def _get_code(value: str):

    cell = {
        "cell_type": "code",
        "source": value,
        "metadata": {},
        "outputs": [],
    }
    return cell
