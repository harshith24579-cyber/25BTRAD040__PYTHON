-- Hospital Appointment Management System - Database Schema (SQLite)
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    age        INTEGER NOT NULL,
    gender     TEXT NOT NULL,
    phone      TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS doctors (
    doctor_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name           TEXT NOT NULL,
    specialization TEXT NOT NULL,
    availability   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id       INTEGER NOT NULL,
    doctor_id        INTEGER NOT NULL,
    appointment_date TEXT NOT NULL,
    appointment_time TEXT NOT NULL,
    status           TEXT NOT NULL DEFAULT 'Booked',
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY(doctor_id)  REFERENCES doctors(doctor_id),
    UNIQUE(doctor_id, appointment_date, appointment_time)
);
