-- Sample data for demonstration / testing (run after schema.sql)
INSERT INTO doctors(name, specialization, availability) VALUES
 ('Dr. Ananya Rao',   'General Medicine', '09:00 AM - 01:00 PM'),
 ('Dr. Rahul Sharma', 'Cardiology',       '10:00 AM - 02:00 PM'),
 ('Dr. Meera Nair',   'Dermatology',      '02:00 PM - 05:00 PM'),
 ('Dr. Arjun Kumar',  'Orthopedics',      '09:00 AM - 12:00 PM'),
 ('Dr. Priya Das',    'Pediatrics',       '11:00 AM - 03:00 PM');

INSERT INTO patients(name, age, gender, phone) VALUES
 ('Rohan Verma', 34, 'Male',   '9876543210'),
 ('Sneha Iyer',  27, 'Female', '9123456780');

INSERT INTO appointments(patient_id, doctor_id, appointment_date, appointment_time) VALUES
 (1, 2, '2026-12-01', '10:00 AM'),
 (2, 3, '2026-12-02', '02:00 PM');
