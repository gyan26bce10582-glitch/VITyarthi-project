def show_attendance(records):
    """Display the attendance list."""

    print(f"\n{'=' * 10} Hostel Attendance {'=' * 10}")

    if not records:
        print("No students registered.")
        return

    for student, status in records.items():
        print(f"{student:<20} -> {status}")

def show_menu():
    """Display the main menu."""

    print("\nHOSTEL ATTENDANCE MENU")
    print("-" * 30)
    print("1. View Attendance")
    print("2. Update Attendance")
    print("3. Add New Student")
    print("4. Exit")

def show_summary(records):
    """Display a simple attendance summary."""

    present = 0
    absent = 0

    for status in records.values():
        if status == "Present":
            present += 1
        elif status == "Absent":
            absent += 1

    print("\nAttendance Summary")
    print("-" * 25)
    print(f"Total Students : {len(records)}")
    print(f"Present        : {present}")
    print(f"Absent         : {absent}")
