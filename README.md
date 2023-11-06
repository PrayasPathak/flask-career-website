# flask-career-website

A career website built using flask.

# Database

The database used in the project is `MySQL`. The script for creation of the database is provided in the `careersdb.sql` file. The name of the database is `careersdb`. To modify the database make modifications to the `careersdb.sql` file.

# Setting up the Project Locally

To set up the database for the project follow the following steps:

- Clone the project
- Create a virtual environment
  - Using conda `conda create -p venv`
  - Using venv `python -m venv venv`
- Install the requirements: `pip install -r requirements.txt`
- Create database for the project using `careersdb.sql` file.
- Set the `DB_CONNECTION_STRING` environment variable to connect to the database.

  - For windows the process is: `set DB_CONNECTION_STRING=mysql+pysql://username:password@localhost/careersdb?charset=utf8mb4`

- Run the application: `python app.py`
