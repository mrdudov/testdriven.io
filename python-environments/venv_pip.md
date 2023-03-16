python -m venv venv
source ./venv/bin/activate
which python
python -m pip freeze > requirements.txt


Want to grab just the top-level dependencies (e.g., requests==2.27.1)? Check out pip-chill. https://pip-chill.readthedocs.io/en/latest/
