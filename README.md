
1. Run development server:
```
python manage.py runserver
```
starts the development server and allows you to access your Django application at http://localhost:8000/ by default.

2. Create a new Django app:
```
python manage.py startapp <app_name>
```
creates a new Django application with the specified `<app_name>`.

3. Create database tables (migrations):
```
python manage.py makemigrations
python manage.py migrate
```
The first command generates database migration files based on the changes in your models. The second command applies those migrations and creates/updates the corresponding database tables.

4. Create a superuser:
```
python manage.py createsuperuser
```
This command prompts you to enter a username, email (optional), and password to create a superuser account. Superusers have administrative access to the Django admin interface.

5. Run tests:
```
python manage.py test
```
This command runs all the tests defined in your Django project.

6. Generate Django shell:
```
python manage.py shell
```
This command opens an interactive Python shell with Django preloaded, allowing you to interact with your project's models and perform database operations.

7. Collect static files:
```
python manage.py collectstatic
```
If you have static files (CSS, JavaScript, images) in your Django project, this command collects them into a single directory defined in your project settings.

These are just a few examples of commonly used `manage.py` commands in Django. There are more commands available, and you can explore them by running `python manage.py --help`.