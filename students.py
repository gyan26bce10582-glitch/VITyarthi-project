def clean_name(name):
    """Remove extra spaces and format the student's name."""
    return name.strip().title()

def register_student(records, name):
    """Register a new student with Present as the default status."""

    name = clean_name(name)

    if name in records:
        return False, "Student already exists."

    records[name] = "Present"
    return True, f"Registered {name}."

def student_exists(records, name):
    """Check whether a student is registered."""

    name = clean_name(name)
    return name in records
