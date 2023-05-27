# https://packaging.python.org/en/latest/tutorials/packaging-projects/
# https://github.com/pypa/twine/issues/424

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --upgrade twine



echo "use __token__ as username"
echo "and token value as password"
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

# python -m twine upload dist/*

