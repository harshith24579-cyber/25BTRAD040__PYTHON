# Hospital Appointment Management System

**Python + Tkinter + SQLite** — Experiential Learning Team Project
Class: AIDE A | Jain University

| Member | USN |
|---|---|
| Harshith | 25BTRAD040 |
| Manu | 25BTRAD063 |
| Vijesh | 25BTRAD04G |
| Edward Philip | 25BTRAD032 |
| Harnish | 25BTRAD016 |

## Features
- Patient registration (name, age, gender, unique phone number) with validation
- Doctor directory (specialization and availability)
- Appointment booking with date validation and double-booking prevention
- Appointment lookup and cancellation by registered phone number
- Administrator dashboard: view all appointments, add doctors

## Project Files
| File | Purpose |
|---|---|
| `expmain.py` | Main application (GUI + database layer) |
| `schema.sql` | Database schema (3 tables) |
| `sample_data.sql` | Optional demo data |
| `test_hospital.py` | Unit tests for the database layer |
| `requirements.txt` | Dependencies (standard library only) |
| `hospital.db` | Created automatically on first run |

## How to Run
```bash
python expmain.py
```
Demo administrator login: `admin` / `admin123`

## Run Tests
```bash
python -m unittest test_hospital -v
```

## Database Design
- **patients** (patient_id PK, name, age, gender, phone UNIQUE)
- **doctors** (doctor_id PK, name, specialization, availability)
- **appointments** (appointment_id PK, patient_id FK, doctor_id FK, date, time, status; UNIQUE on doctor + date + time)

Relationships: one patient → many appointments; one doctor → many appointments.

## Limitations / Future Work
- Admin credentials are hardcoded (demo only); use hashed passwords in a real system
- Patients identified by phone number only (no login/OTP)
- Availability is free text; booked slots are not checked against it
- Possible additions: email/SMS reminders, doctor login, reports, appointment rescheduling

*Educational demonstration, not a production hospital system.*
