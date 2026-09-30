def valid_menu_choice(choice):
    """Check whether the menu choice is valid."""
    return choice in ("1", "2", "3", "4")

def valid_attendance_status(status):
    """Check whether the attendance status is valid."""
    status = status.strip().title()
    return status in ("Present", "Absent")

def get_student_name():
    """Get and format a student name from the user."""

    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name.title()

        print("Student name cannot be empty.")

def get_attendance_status():
    """Get a valid attendance status from the user."""

    while True:
        status = input("Change to (Present/Absent): ").strip().title()

        if valid_attendance_status(status):
            return status

        print("Invalid input. Please enter Present or Absent.")# validation.py

def valid_menu_choice(choice):
    """Check whether the menu choice is valid."""
    return choice in ("1", "2", "3", "4")

def valid_attendance_status(status):
    """Check whether the attendance status is valid."""
    status = status.strip().title()
    return status in ("Present", "Absent")

def get_student_name():
    """Get and format a student name from the user."""

    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name.title()

        print("Student name cannot be empty.")

def get_attendance_status():
    """Get a valid attendance status from the user."""

    while True:
        status = input("Change to (Present/Absent): ").strip().title()

        if valid_attendance_status(status):
            return status

        print("Invalid input. Please enter Present or Absent.")
