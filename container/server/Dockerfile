FROM python:3.8
WORKDIR /var/www/html
RUN pip install fastapi uvicorn sqlalchemy mysqlclient flake8 autopep8 bcrypt pytest sqlalchemy_utils pytest-watch requests
# passlib?
CMD  ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9004", "--reload"]