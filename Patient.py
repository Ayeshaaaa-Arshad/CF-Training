class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"Patient: {self.name} Status: {self.status}\n"

    def __format__(self, format_spec):
        # Get the Description based on format_specifications
        if format_spec == "brief":
            return f"{self.name}: {self.status.name}"
        elif format_spec == "detailed":
            return f"Patient {self.name} is in {self.status.name} stage"
        else:
            return f"Patient {self.name} ({self.status.name})"
