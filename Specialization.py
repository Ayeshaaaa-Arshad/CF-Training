import os


class Specialization:
    FILE_NAME = "Patients.txt"

    @staticmethod
    def add_patient(patient):
        with open(Specialization.FILE_NAME, 'a') as f:
            f.write(str(patient))

    @staticmethod
    def retrieve_next_patient():
        with open(Specialization.FILE_NAME, 'r') as f:
            records = f.readlines()
            try:
                # Splitting records based on format as 2nd index after splitting contains name
                print(records[0].split(' ')[1])
            except Exception as e:
                print(e)

    @staticmethod
    def remove_patient_by_name(name):
        Flag = True

        # Reading all records from file and save in List
        with open(Specialization.FILE_NAME, 'r') as f:
            records = f.readlines()
            try:
                for index, patient in enumerate(records):
                    if records[index].split(' ')[1].lower() == name.lower():
                        records.pop(index)
                        Flag = False
                        print(f"Patient has {name} is deleted from Queue\n")
                        with open("Patient2.txt", 'w') as file:
                            file.writelines(records)

                            # Removing previous File in order to update the contents
                            file_path = Specialization.FILE_NAME
                            if os.path.exists(Specialization.FILE_NAME):
                                os.remove(file_path)

                            # Updating the name of new file
                            if os.path.exists("Patient2.txt"):
                                os.rename("Patient2.txt", "Patients.txt")
                if Flag:
                    print(f"No Such Patient found")
            except Exception as e:
                print(e)
