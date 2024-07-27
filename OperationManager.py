import Specialization


class OperationManager:
    @staticmethod
    def add_specialization(patient):
        Specialization.Specialization.add_patient(patient)

    @staticmethod
    def list_specialization():
        with open(Specialization.Specialization.FILE_NAME, 'r') as f:
            records = f.readlines()
            try:
                for patient in records:
                    print(patient)
            except Exception as e:
                print(e)
                print("Error in Listing Patients")

    @staticmethod
    def retrieve_next_patient():
        Specialization.Specialization.retrieve_next_patient()

    @staticmethod
    def remove_patient_by_name(patient_name):
        Specialization.Specialization.remove_patient_by_name(patient_name)
