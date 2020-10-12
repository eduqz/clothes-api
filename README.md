# Clothes API
## Introduction
This project is created to assist in learning about [**FastAPI**](https://fastapi.tiangolo.com/). It is a simple API example, for clothing list management.

## Technologies
This is a web application writted in Python using [**FastAPI**](https://fastapi.tiangolo.com/) as framework and [**SQLAlchemy**](https://www.sqlalchemy.org/) as ORM. In my tests,
I also used a [**PostgreSQL**](https://www.postgresql.org/) database.

## How to run
### Setup the enviroment (when running for the first time)
1. Use `virtualenv venv -p python3` to create a python virtual environment to your project. Learn more about it [here](https://realpython.com/python-virtual-environments-a-primer/)
2. Use `source venv /bin/activate` to activate the virtual environment
3. Use `pip install -r requirements.txt` to install all the required packages

### Running the applicaiton
1. Use `uvicorn main:app --reload` to run the application
2. Open [http://localhost:8000/docs](http://localhost:8000/docs) to view the API documentation and test the methods.
