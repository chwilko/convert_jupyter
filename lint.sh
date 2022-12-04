poetry run black .  --exclude="tests/code"
poetry run isort .
poetry run mypy . --exclude="tests/code"
poetry run flake8 . --exclude="tests/code"
poetry run pylint .