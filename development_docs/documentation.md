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

- Don’t repeat yourself (DRY): Every distinct concept and/or piece of data should live in one, and only one, place. Redundancy is bad. Normalization is good.

- Explicit is better than implicit: Django shouldn’t do too much “magic”. Magic shouldn’t happen unless there’s a really good reason for it. Magic is worth using only if it creates a huge convenience unattainable in other ways, and it isn’t implemented in a way that confuses developers who are trying to learn how to use the feature.

- Loose coupling: The various layers of the framework shouldn’t “know” about each other unless absolutely necessary. For example, the template system knows nothing about web requests, the database layer knows nothing about data display and the view system doesn’t care which template system a programmer uses. Although Django comes with a full stack for convenience, the pieces of the stack are independent of another wherever possible.
  
- Consistency: The framework should be consistent at all levels. Consistency applies to everything from low-level (the Python coding style used) to high-level (the “experience” of using Django).
 
- Leverage Python’s features: Django should take full advantage of Python’s dynamic capabilities, such as introspection. Django apps should use as little code as possible; they should lack boilerplate.

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
  * add the JWT token in the Authorization header
  * give the employee id in the url
  * success response 200:
    ```json
    {
      "id": 101,
      "department": {
        "id": 5,
        "department_name": "Engineering"
      },
      "legal_first_name": "Jane",
      "legal_last_name": "Smith",
      "pref_first_name": "Janie",
      "pref_last_name": "Smith",
      "NIC": "9876543210",
      "email": "jane.smith@example.com",
      "age": 35,
      "gender": "Female",
      "dob": "1987-02-15",
      "country_of_birth": "USA",
      "marital_status": "Married",
      "ethnicity": "Caucasian",
      "nationality": "American",
      "citizenship_status": "Citizen",
      "address": "123 Main St, Anytown, USA",
      "phone": "5551234567",
      "emmergency_contact": "5559876543"
    }
    ```
  * error response 404 not found:
    ```json
    {
      "message": "The employee does not exist",
      "error": "Employee matching query does not exist."
    }
    ```
- **GET** `http://localhost:8000/api/employees/`: Retrieve a list of all employees.
  * this will basically returns all the employees in the system database
  * success response 200:
    ```json
    [
      {
        "id": 101,
        "department": {
          "id": 5,
          "department_name": "Engineering"
        },
        "legal_first_name": "Jane",
        "legal_last_name": "Smith",
        "pref_first_name": "Janie",
        "pref_last_name": "Smith",
        "NIC": "9876543210",
        "email": "jane.smith@example.com",
        "age": 35,
        "gender": "Female",
        "dob": "1987-02-15",
        "country_of_birth": "USA",
        "marital_status": "Married",
        "ethnicity": "Caucasian",
        "nationality": "American",
        "citizenship_status": "Citizen",
        "address": "123 Main St, Anytown, USA",
        "phone": "5551234567",
        "emmergency_contact": "5559876543"
      }
    ]
    ```

#### Request Management

- **GET** `http://localhost:8000/api/request/{id}`: Retrieve the details of a single request.
  * add the JWT token in the Authorization header
  * give the request id in the url
  * success response 200:
    ```json
    {
      "id": 1,
      "request_type": "Type1",
      "request_name": "Request1",
      "details": "Details about request1",
      "employee": 1
    }
    ```
  * error response 404 not found:
    ```json
    {
      "message": "The request does not exist",
      "error": "Request matching query does not exist."
    }
    ```
- **GET** `http://localhost:8000/api/requests/`: Retrieve a list of all requests.
  * this will basically returns all the requests in the system database
  * success response 200:
    ```json
    [
      {
        "id": 1,
        "request_type": "Type1",
        "request_name": "Request1",
        "details": "Details about request1",
        "employee": 1
      }
    ]
    ```
- **GET** `http://localhost:8000/api/employee/{id}/requests`: Retrieve a list of all requests for a specific employee.
  * add the JWT token in the Authorization header
  * give the employee id in the url
  * success response 200:
    ```json
    [
      {
        "id": 1,
        "request_type": "Type1",
        "request_name": "Request1",
        "details": "Details about request1",
        "employee": 1
      }
    ]
    ```
  * error response 404 not found:
    ```json
    {
      "message": "The employee does not exist",
      "error": "Employee matching query does not exist."
    }
    ```

#### Document Management

- **GET** `http://localhost:8000/api/document/{id}`: Retrieve the details of a single document.
- **GET** `http://localhost:8000/api/documents/`: Retrieve a list of all documents.
- **GET** `http://localhost:8000/api/employee/{id}/documents`: Retrieve a list of all documents for a specific employee.
- **POST** `http://localhost:8000/api/document/upload/`: Upload a new document.
  * add the JWT token in the Authorization header
  * request - add data in form-data format
    form-fields:
    ```form-data
    file: <file>: File
    description: <description>: Text
    document_category: <document_category>: Text
    employee: <employee_id>: Text
    ```
  * success response 201:
    ```json
    {
      "name_doc": "Resume.pdf",
      "description": "Some description",
      "uploaded_date": "2023-12-26",
      "updated_date": "2023-12-26",
      "document_category": "Some category",
      "doc_link": "document/data/Resume.pdf",
      "employee": 2
    }
    ```

### Codebase structure

- **this project strickly follows the Django folder structure and best practices**

### Database Schema

you can find the database schema here 
![Database Schema](development_docs/er_diagram.png)

### Configuration

### Troubleshooting

### Testing







