fill() {
    local text="$1"
    local fill_char="$2"
    local columns=$(tput cols)
    local stars=$(( (columns - ${#text}) / 2  - 1))
    printf '%.s*' $(seq 1 $stars) 
    printf " "
    printf $text
    printf " "
    printf '%.s*' $(seq 1 $stars)
    printf "\n"
}

fill "BLACK" "*"
poetry run black .  --exclude="tests/code"
fill "ISORT" "*"
poetry run isort .
fill "MYPY" "*"
poetry run mypy . --exclude="tests/code"
fill "FLAKE8" "*"
poetry run flake8 . --exclude="tests/code"
fill "PYLINT" "*"
poetry run pylint convert_jupyter
