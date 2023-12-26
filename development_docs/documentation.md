### Overview

Purpose of this project is to provide a backend service to manage employee self service related activities. including but not limited to:

- Employee profile management(personal details, contact details, emergency contact details, bank details, etc.)
- View performance review details, feedbacks, etc.
- Manage leave requests and other requests
- Access company handbook, policies, etc.

### Architecture

This project is build using Django framework. It uses Django Rest Framework to provide Rest API endpoints. It uses Mysql Database to persist data. as the authentication mechanism it uses JWT tokens.

this project consist of multiple apps which are responsible for different functionalities of the entities in the system such as employee, leave, etc. having multiple application promotes the separation of conserns and makes the codebase more maintainable.

this project strickly follows the Django best practices and the codebase is structured in a way that it is easy to understand and maintain. in order to understand the Django API development please refer to the official documentation of Django [https://www.django-rest-framework.org/].

### Design principles

since this project is build using Django framework, it follows the Django best practices and design principles. some of the key design principles are:

- Separation of conserns
- DRY(Don't repeat yourself)
- KISS(Keep it simple, stupid)
- YAGNI(You aren't gonna need it)
- Convention over configuration
- etc.

### Features

- Employee profile information management
- Leave management
- Performance review management - ***tobe implemented***
- Company handbook management - ***tobe implemented***
- Employee Documents management

### API Documentation

#### User Management

- **POST** `http://localhost:8000/api/signup/`: Create a new user account.
  * request body:
    ```json
    {
        "username": "testuser",
        "password": "testpassword",
        "email": "name@email_domain.com",
    }
    ```
  * success response 201:
    ```json
    {
        "username": "testuser",
        "email": "name@email_domain.com"
    } 
    ```
  * error response 400:
    ```json
    {
        "username": [
            "A user with that username already exists."
        ]
    }
    ```
- **POST** `http://localhost:8000/api/login/`: Log in to a user account.
  * ***JWT token authentication is being used for this endpoint***
  * request body:
    ```json
    {
        "username": "testuser",
        "password": "testpassword"
    }
    ```
  * success response 200:
    ```json
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
    ```
  * error response 401 unauthorised:
    ```json
    {
        "status": "Invalid credentials"
    }
    ```
  * ***use the token in the response to authenticate the requests to the protected endpoints via Authorization header*** 
  
- **POST** `http://localhost:8000/api/logout/`: Log out of a user account.
  * send the JWT token in the Authorization header
  * success response 200:
    ```json
    {
        "status": "Logout successful."
    }
    ```
  * error response 401 unauthorised:
    ```json
    {
    "detail": "Invalid token."
    }
    ```

#### Employee Management

- **GET** `http://localhost:8000/api/employee/{id}`: Retrieve the details of a single employee.
- **GET** `http://localhost:8000/api/employees/`: Retrieve a list of all employees.

#### Request Management

- **GET** `http://localhost:8000/api/request/{id}`: Retrieve the details of a single request.
- **GET** `http://localhost:8000/api/requests/`: Retrieve a list of all requests.
- **GET** `http://localhost:8000/api/employee/{id}/requests`: Retrieve a list of all requests for a specific employee.

#### Document Management

- **GET** `http://localhost:8000/api/document/{id}`: Retrieve the details of a single document.
- **GET** `http://localhost:8000/api/documents/`: Retrieve a list of all documents.
- **GET** `http://localhost:8000/api/employee/{id}/documents`: Retrieve a list of all documents for a specific employee.
- **POST** `http://localhost:8000/api/document/upload/`: Upload a new document.



