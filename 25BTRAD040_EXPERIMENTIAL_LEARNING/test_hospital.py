"""Unit tests for the HospitalDB layer.  Run: python -m unittest test_hospital -v"""
import sqlite3
import sys
import types
import unittest

# Allow the DB tests to run on machines without tkinter (e.g. servers/CI).
try:
    import tkinter  # noqa: F401
except ImportError:
    tk = types.ModuleType("tkinter")
    tk.ttk = tk.messagebox = tk.simpledialog = types.ModuleType("stub")
    sys.modules.update({"tkinter": tk, "tkinter.ttk": tk.ttk,
                        "tkinter.messagebox": tk.messagebox,
                        "tkinter.simpledialog": tk.simpledialog})

from expmain import HospitalDB


class HospitalDBTests(unittest.TestCase):
    def setUp(self):
        self.db = HospitalDB(":memory:")          # fresh in-memory DB per test
        self.pid = self.db.register_patient("Test Patient", 30, "Male", "9999900000")
        self.doc = self.db.get_doctors()[0][0]

    def tearDown(self):
        self.db.close()

    def test_doctors_seeded(self):
        self.assertEqual(len(self.db.get_doctors()), 5)

    def test_seed_not_duplicated(self):
        self.db.seed_doctors()
        self.assertEqual(len(self.db.get_doctors()), 5)

    def test_register_and_lookup_patient(self):
        p = self.db.get_patient_by_phone("9999900000")
        self.assertEqual(p[1], "Test Patient")
        self.assertIsNone(self.db.get_patient_by_phone("0000000000"))

    def test_duplicate_phone_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.register_patient("Other", 22, "Female", "9999900000")

    def test_book_appointment(self):
        aid = self.db.book(self.pid, self.doc, "2030-01-01", "10:00 AM")
        rows = self.db.patient_appointments("9999900000")
        self.assertEqual(rows[0][0], aid)
        self.assertEqual(rows[0][5], "Booked")

    def test_double_booking_rejected(self):
        self.db.book(self.pid, self.doc, "2030-01-01", "10:00 AM")
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.book(self.pid, self.doc, "2030-01-01", "10:00 AM")

    def test_invalid_doctor_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.book(self.pid, 999, "2030-01-01", "10:00 AM")

    def test_cancel_by_owner(self):
        aid = self.db.book(self.pid, self.doc, "2030-01-01", "10:00 AM")
        self.assertEqual(self.db.cancel_patient_appointment(aid, "9999900000"), 1)
        self.assertEqual(self.db.patient_appointments("9999900000")[0][5], "Cancelled")

    def test_cancel_by_other_patient_blocked(self):
        self.db.register_patient("Other", 40, "Female", "8888800000")
        aid = self.db.book(self.pid, self.doc, "2030-01-01", "10:00 AM")
        self.assertEqual(self.db.cancel_patient_appointment(aid, "8888800000"), 0)

    def test_add_doctor_and_all_appointments(self):
        self.db.add_doctor("Dr. New", "ENT", "09:00 AM - 11:00 AM")
        self.assertEqual(len(self.db.get_doctors()), 6)
        self.db.book(self.pid, self.doc, "2030-01-01", "10:00 AM")
        self.assertEqual(len(self.db.all_appointments()), 1)


if __name__ == "__main__":
    unittest.main()
