from collections import OrderedDict
import os
from django.test import TestCase

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'self_service_portal.settings'

import django
django.setup()

from employee.models import Department, Employee
from employee.serializer import EmployeeSerializer



class EmployeeTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(department_name='IT')
        self.employee = Employee.objects.create(
            legal_first_name='John',
            legal_last_name='Doe',
            pref_first_name='John',
            pref_last_name='D',
            NIC='123456789',
            email='john@example.com',
            age=30,
            gender='Male',
            dob='1992-01-01',
            country_of_birth='United States',
            marital_status='Single',
            ethnicity='Caucasian',
            nationality='American',
            citizenship_status='Citizen',
            department=self.department,
            address='123 Main St',
            phone='1234567890'
        )

    def test_employee_serializer(self):
        serializer = EmployeeSerializer(instance=self.employee)
        expected_data = {
            'id': 13, 
            'department': OrderedDict([('id', 9), ('department_name', 'IT')]), 
            'legal_first_name': 'John', 
            'legal_last_name': 'Doe', 
            'pref_first_name': 'John', 
            'pref_last_name': 'D', 
            'NIC': '123456789', 
            'email': 'john@example.com',
            'age': 30, 
            'gender': 'Male', 
            'dob': '1992-01-01', 
            'country_of_birth': 'United States', 
            'marital_status': 'Single', 
            'ethnicity': 'Caucasian', 
            'nationality': 'American', 
            'citizenship_status': 'Citizen', 
            'address': '123 Main St', 
            'phone': '1234567890'
            }
        print(expected_data)
        self.assertEqual(serializer.data, expected_data)

    # def test_employees_list_view(self):
    #     response = self.client.get('/employees/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), 1)

    # def test_employee_detail_view(self):
    #     response = self.client.get(f'/employees/{self.employee.id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['id'], self.employee.id)

    # def test_request_delete_data_view(self):
    #     response = self.client.delete(f'/employees/{self.employee.id}/')
    #     self.assertEqual(response.status_code, 204)
    #     self.assertFalse(Employee.objects.filter(id=self.employee.id).exists())
