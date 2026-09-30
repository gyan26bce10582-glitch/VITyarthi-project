# attendance.py

def update_attendance(records, name, new_status):
    """Update the attendance status of a student."""

    name = name.strip().title()
    new_status = new_status.strip().title()

    if name not in records:
        return False, f"'{name}' is not registered."

    if new_status not in ("Present", "Absent"):
        return False, "Invalid attendance status."

    records[name] = new_status

    return True, "Status updated successfully."


def get_attendance(records, name):
    """Return the attendance status of a student."""

    name = name.strip().title()

    if name not in records:
        return None

    return records[name]


def count_attendance(records):
    """Count the number of present and absent students."""

    present = 0
    absent = 0

    for status in records.values():
        if status == "Present":
            present += 1
        elif status == "Absent":
            absent += 1

    return present, absent