INSERT INTO public.employee_department (department_name)
VALUES
    ('HR'),
    ('IT'),
    ('Finance');


INSERT INTO public.employee_employee (
    legal_first_name,
    legal_last_name,
    pref_first_name,
    pref_last_name,
    "NIC",
    email,
    age,
    gender,
    dob,
    country_of_birth,
    marital_status,
    ethnicity,
    nationality,
    citizenship_status,
    address,
    phone,
    department_id
)
VALUES
    ('John', 'Smith', 'Johnny', 'J. Smith', '1234', 'john.smith@example.com', 30, 'Male', '1993-06-15', 'USA', 'Single', 'Caucasian', 'American', 'Citizen', '123 Main St, Anytown, USA', '+1 123 4567', 1),
    ('Jane', 'Doe', 'Janey', 'J. Doe', '5678', 'jane.doe@example.com', 28, 'Female', '1995-03-22', 'Canada', 'Married', 'Asian', 'Canadian', 'Permanent Resident', '456 Elm St, Othertown, CA', '+1 987 6543', 2),
    ('Mike', 'Johnson', 'Mickey', 'M. Johnson', '9012', 'mike.johnson@example.com', 35, 'Male', '1988-11-10', 'UK', 'Divorced', 'African', 'British', 'Non-Citizen', '789 Oak Ave, Anycity, UK', '+44 20 1234', 1);

INSERT INTO public.document_document (
    name_doc,
    description,
    uploaded_date,
    updated_date,
    document_category,
    doc_link,
    employee_id
)
VALUES
    ('Contract 2023', 'Employment Contract', '2023-07-15', '2023-07-17', 'Employment', '/documents/contract_2023', 1),
    ('Passport Scan', 'Passport Copy', '2023-07-10', '2023-07-11', 'Identification', '/documents/passport_scan', 2),
    ('Training Plan', 'Training Document', '2023-07-20', '2023-07-21', 'Training', '/documents/training_plan', 1);


INSERT INTO public."Request_request" (
    request_type,
    request_name,
    details,
    employee_id
)
VALUES
    ('Leave', 'Annual Leave', 'Requesting 5 days of annual leave', 1),
    ('Promotion', 'Senior Developer', 'Requesting a promotion to senior', 3),
    ('Expense', 'Conference Travel', 'Requesting expense for conference', 2);
