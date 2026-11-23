# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# MINI PROJECT (UNIT 3) - Problem Solving Component
# Program 5: Attendance Tracker (Lists and Dictionaries)

# Data structure: dictionary -> {student_name: [list of "P"/"A" records]}

def add_student(attendance, name):
    """Add a new student with an empty attendance list."""
    if name in attendance:
        print(f"  '{name}' already exists.")
    else:
        attendance[name] = []
        print(f"  Student '{name}' added.")


def mark_attendance(attendance, name, status):
    """Add a new day's attendance ('P' or 'A') for a student."""
    status = status.upper()
    if name not in attendance:
        print(f"  '{name}' not found.")
    elif status not in ("P", "A"):
        print("  Status must be 'P' (Present) or 'A' (Absent).")
    else:
        attendance[name].append(status)
        print(f"  Marked {name} as {status}.")


def update_attendance(attendance, name, day, status):
    """Update an existing day's (1-based) attendance status."""
    status = status.upper()
    if name not in attendance:
        print(f"  '{name}' not found.")
    elif status not in ("P", "A"):
        print("  Status must be 'P' or 'A'.")
    elif not 1 <= day <= len(attendance[name]):
        print(f"  Day {day} is invalid for {name}.")
    else:
        attendance[name][day - 1] = status
        print(f"  Updated {name}, day {day} -> {status}.")


def attendance_percentage(records):
    """Return attendance percentage for a list of 'P'/'A' records."""
    if not records:
        return 0.0
    return records.count("P") / len(records) * 100


def display_attendance(attendance):
    """Display records in an organised table."""
    print("\n  {:<12} {:<22} {:>8}".format("Student", "Record", "Percent"))
    print("  " + "-" * 44)
    for name, records in attendance.items():
        print("  {:<12} {:<22} {:>7.2f}%".format(
            name, " ".join(records) if records else "-",
            attendance_percentage(records)))


def below_threshold(attendance, threshold):
    """Return list of (name, percent) for students below threshold."""
    return [(n, attendance_percentage(r)) for n, r in attendance.items()
            if attendance_percentage(r) < threshold]


def test_attendance():
    print("=" * 50)
    print("PART 1: ATTENDANCE TRACKER")
    print("=" * 50)
    attendance = {}

    # Scenario 1: add students
    print("\n[Scenario 1] Adding students")
    for s in ["Asha", "Bharath", "Chitra", "Dev"]:
        add_student(attendance, s)
    add_student(attendance, "Asha")          # duplicate

    # Scenario 2: mark attendance over 5 days
    print("\n[Scenario 2] Marking attendance for 5 days")
    data = {
        "Asha":    ["P", "P", "P", "P", "P"],   # 100%
        "Bharath": ["P", "A", "P", "A", "P"],   # 60%
        "Chitra":  ["A", "A", "P", "A", "A"],   # 20%
        "Dev":     ["P", "P", "P", "A", "P"],   # 80%
    }
    for name, recs in data.items():
        for r in recs:
            attendance[name].append(r)
    display_attendance(attendance)

    # Scenario 3: update + invalid inputs
    print("\n[Scenario 3] Updating records and invalid inputs")
    update_attendance(attendance, "Chitra", 1, "P")   # A -> P
    update_attendance(attendance, "Chitra", 9, "P")   # bad day
    update_attendance(attendance, "Zed", 1, "P")      # unknown student
    mark_attendance(attendance, "Dev", "X")           # bad status
    display_attendance(attendance)

    # Scenario 4: threshold check
    print("\n[Scenario 4] Students below 75% attendance")
    for name, pct in below_threshold(attendance, 75):
        print(f"  {name}: {pct:.2f}%  <-- SHORTAGE")

    print("\n[Scenario 5] Students below 50% attendance")
    low = below_threshold(attendance, 50)
    if low:
        for name, pct in low:
            print(f"  {name}: {pct:.2f}%")
    else:
        print("  None")

    # Scenario 6: edge case - student with no records
    print("\n[Scenario 6] New student with no records")
    add_student(attendance, "Esha")
    display_attendance(attendance)


if __name__ == "__main__":
    test_attendance()
