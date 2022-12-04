import json

CEIL_SEPARATOR = "# New cell"
MARKDOWN_BEGIN = "'''md\n"
MARKDOWN_END = "\n'''"


f_in = open("scripts/reaserch/try.ipynb", "r")
f_out = open("scripts/reaserch/try.py", "w")

my_file = json.load(f_in)

for cell in my_file["cells"]:
    print(CEIL_SEPARATOR, file=f_out)
    if cell["cell_type"] == "code":
        print(*cell["source"], sep="", file=f_out)
    elif cell["cell_type"] == "markdown":
        print(
            MARKDOWN_BEGIN,
            *cell["source"],
            MARKDOWN_END,
            sep="",
            file=f_out,
        )
