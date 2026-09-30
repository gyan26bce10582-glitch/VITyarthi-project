from attendance import update_attendance, get_attendance
from students import register_student
from validation import get_student_name, get_attendance_status
from display import show_attendance, show_menu, show_summary

# Starting data. The names go through .title() so they always match the
# way names get cleaned up when someone types them in.
records = {
    name.title(): status
    for name, status in {
        "Ekansh Gupta": "Present",
        "Lakshay Kumar": "Present",
        "Bhavya": "Absent",
        "Raghav": "Absent",
    }.items()
}


def update_student_attendance():
    """Ask for a name and change that student's attendance."""
    name = get_student_name()
    current_status = get_attendance(records, name)

    # Can't update someone who isn't in the list yet
    if current_status is None:
        print(f"'{name}' isn't registered yet. Add them from the menu first.")
        return

    print(f"Current status: {current_status}")
    new_status = get_attendance_status()

    _, message = update_attendance(records, name, new_status)
    print(message)


def add_student():
    """Register a new student."""
    name = get_student_name()
    _, message = register_student(records, name)
    print(message)


def main():
    """Run the hostel attendance menu until the user quits."""
    while True:
        show_menu()

        try:
            choice = input("Select an option: ").strip()
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C / Ctrl+D: leave the same way as the normal exit
            print("\nExiting...")
            choice = "4"

        if choice == "1":
            show_attendance(records)
        elif choice == "2":
            update_student_attendance()
        elif choice == "3":
            add_student()
        elif choice == "4":
            show_summary(records)
            print("\nAttendance system closed.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()