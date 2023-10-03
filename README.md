# Todo List Backend

This is a simple todo list API built with Django Rest Framework. It also has user authentication.

## .env File
The .env file contains environment variables that are used to configure the application. You should create a .env file in the project root directory and add the following variables:

* SECRET_KEY - A secret key used for authentication and encryption.
* DEBUG - Set to 1 if you want to enable debugging mode.
* ALLOWED_HOSTS - A space-separated list of hostnames that are allowed to access the application.

## Installation
1. Clone the repository: `git clone https://github.com/Skapupel/todolist_django`
2. Install the requirements: `pip install -r requirements.txt`
3. Configure .env File
4. Create the database: `python manage.py migrate`
5. Run the server: `python manage.py runserver`

## Documentation
Once the server is running, you can access the API documentation at `http://localhost:8000/schema/swagger-ui/`
