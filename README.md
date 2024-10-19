TIME MANAGEMENT API
This is a Time Management API built using Django and Django REST Framework (DRF). 
It allows users to manage tasks and provides JWT authentication for user access. 
The API includes endpoints for managing tasks and user authentication, including obtaining and refreshing tokens.

FEATURES
User authentication using JWT (JSON Web Token).
Task management: create, read, update, and delete tasks.
API endpoints for task and user management.
Secure access to API resources.

PROJECT STRUCTURE
Django: Backend framework used for building the API.
Django REST Framework: Provides API development functionality and tools.
JWT Authentication: Secures user access with token-based authentication.

REQUIREMENTS
To run this project, you will need to have installed the following:

Python 3.x
Django
Django REST Framework
SimpleJWT (for JWT authentication)
You can find all the dependencies listed in the requirements.txt file

INSTALLATION.
Follow these steps to set up the project locally:

1.Clone the repository:
git clone <repository-url>
cd time-management-api

2. Create and activate a virtual environment:
For Windows run:
.\env\Scripts\activate

On Linux/macOS run:
source env/bin/activate

3. Install the required dependencies:
pip install djangorestframework-simplejwt

4. Apply the migrations:
   python manage.py migrate

5.Create a superuser for accessing the Django admin:  # add your details
python manage.py createsuperuser

6.Run the development server:
python manage.py runserver

You can now access the API at http://127.0.0.1:8000/api/

API ENDPOINTS
Method	               Endpoint	                               Description
POST	                 /api/token/	                       Obtain JWT token (login)
POST	                 /api/token/refresh/	               Refresh JWT token
GET	                   /api/tasks/	                       Get the list of tasks
POST	                 /api/tasks/	                       Create a new task
GET	                   /api/tasks/<id>/	                   Get details of a specific task
PUT	                   /api/tasks/<id>/	                   Update a specific task
DELETE	               /api/tasks/<id>/	                   Delete a specific task
GET	                   /api/users/	                       Get the list of users (admin only)

AUTHENTICATION
The API uses JWT for authentication.
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MTcwMjExLCJpYXQiOjE3MjkxNjY2MTEsImp0aSI6Ijg5NmJlYWYwODJmZTRmMjk5YzFmNmZiMmVmZDk5M2E5IiwidXNlcl9pZCI6Mn0.N9OYk4odCklLgkrj0pYPXG0eewk2ojllT6EmnrKMyoE
