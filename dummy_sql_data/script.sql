-- Insert into Department
INSERT INTO employee_department  (department_name)
VALUES ('Department1'),
       ('Department2'),
       ('Department3');
      
SELECT * FROM employee_employee;

-- Insert into Employee
INSERT INTO employee_employee  (legal_first_name, legal_last_name, pref_first_name, pref_last_name, NIC, email, age, gender, dob, country_of_birth, marital_status, ethnicity, nationality, citizenship_status, department_id, address, phone, emmergency_contact)
VALUES ('John', 'Doe', 'John', 'Doe', '1234567890', 'john.doe@example.com', 30, 'Male', '1992-01-01', 'Country1', 'Single', 'Ethnicity1', 'Nationality1', 'Citizenship1', 1, 'Address1', '1234567890', '0987654321'),
       ('Jane', 'Doe', 'Jane', 'Doe', '0987654321', 'jane.doe@example.com', 25, 'Female', '1997-01-01', 'Country2', 'Married', 'Ethnicity2', 'Nationality2', 'Citizenship2', 2, 'Address2', '0987654321', '1234567890');
       
      
INSERT INTO document_document  (name_doc, description, uploaded_date, updated_date, document_category, doc_link, employee_id)
VALUES ('Doc1', 'Description1', '2022-01-01', '2022-01-02', 'Category1', 'http://link1.com', 1),
       ('Doc2', 'Description2', '2022-02-01', '2022-02-02', 'Category2', 'http://link2.com', 2),
       ('Doc3', 'Description3', '2022-03-01', '2022-03-02', 'Category3', 'http://link3.com', 1);
       
      
INSERT INTO Request_request  (request_type, request_name, details, employee_id)
VALUES ('Type1', 'Request1', 'Details about request1', 1),
       ('Type2', 'Request2', 'Details about request2', 2),
       ('Type3', 'Request3', 'Details about request3', 2);