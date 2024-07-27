"""
Hospital Patient Queue Management System:
The Hospital Patient Queue Management System is a Python-based command-line application designed to manage patient queues in a hospital.
It utilizes object-oriented programming (OOP) principles and includes three main classes: Patient, Specialization, and OperationsManager.
This project provides a simple yet effective way to handle patient data and queue management within a hospital setting.
The Hospital Patient Queue Management System is an illustration of OOP concepts in Python. It consists of three primary classes,
each serving a specific purpose:

Patient:
The Patient class represents an individual patient and includes the following attributes:
name: The name of the patient.
status: The patient's status, which can be 0 (normal), 1 (urgent), or 2 (super-urgent).
This class provides methods for string representation and status formatting for patients.

Specialization;
The Specialization class manages patient queues within different specializations. It offers functionalities such as:
Adding patients with various urgency levels.
Retrieving the next patient from the queue.
Removing patients by name.
Checking queue capacity.

OperationsManager:
The OperationsManager class serves as the user interface for interacting with the Specialization instances. Users can perform actions like:
Adding new patients to specializations.
Listing patients in specializations.
Retrieving the next patient.
Removing patients.
Ending the program gracefully.

Note: Please make sure to use below concepts in the above projects:
1. File handling to store and read data.
2. Exception Handling
3. Add proper comments to the code

"""
import Patient
import Status
import OperationManager

# Driver Function
if __name__ == "__main__":
    while True:
        print("1. Add a Patient\n"
              "2. List all Patients\n"
              "3. Retrieve next Patient from queue\n"
              "4. Remove Patient by name\n"
              "5. Exit")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if option == 1:
            name = input("Enter Name of Patient: ")
            while True:
                try:
                    status = int(input("Enter Status\n"
                                       "0. Normal\n"
                                       "1. Urgent\n"
                                       "2. Super_Urgent\n"))
                    if status in [0, 1, 2]:
                        break
                    else:
                        print("Invalid status. Please enter 0, 1, or 2.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            p = Patient.Patient(name, Status.Status(status).name)
            OperationManager.OperationManager.add_specialization(p)

        elif option == 2:
            OperationManager.OperationManager.list_specialization()

        elif option == 3:
            OperationManager.OperationManager.retrieve_next_patient()

        elif option == 4:
            name = input("Enter Name of Patient you want to remove: ")
            OperationManager.OperationManager.remove_patient_by_name(name)

        elif option == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
