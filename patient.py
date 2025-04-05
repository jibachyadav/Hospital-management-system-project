class Patient:
   
    def __init__(self, first_name, surname, age, mobile, postcode, address, symptoms, doctor='None'):
        self._first_name = first_name
        self._surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__address = address
        self.__symptoms = symptoms if isinstance(symptoms, list) else symptoms.split(', ')
        self.__doctor = doctor
        self.appointments = []

    def get_first_name(self):
        return self._first_name

    def get_surname(self):
        return self._surname

    def full_name(self):
        return f"{self._first_name} {self._surname}"

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor, appointment_date):
        self.__doctor = doctor
        self.appointment_date = appointment_date

    def print_symptoms(self):
        print(", ".join(self.__symptoms))

    def add_symptoms(self, new_symptoms):
        if isinstance(new_symptoms, list):
            self.__symptoms.extend(new_symptoms)
        else:
            self.__symptoms.append(new_symptoms)

    def get_symptoms(self):
        return self.__symptoms

    def add_appointment(self, time):
        self.appointments.append(time)
        self.status = "Approved"

    @staticmethod
    def read_patient_records(patients_file: str) -> list:
        patient_list = []
        try:
            with open(patients_file, 'r') as fd:
                for line in fd:
                    data = line.split('|')
                    firstname = data[0].strip().split(" ")[0]
                    surname = data[0].strip().split(" ")[1]
                    patient = Patient(
                        firstname.strip(),
                        surname.strip(),
                        int(data[1].strip()),
                        data[2].strip(),
                        data[3].strip(),
                        data[4].strip(),
                        data[5].strip().split(', '),
                        data[6].strip())
                    patient_list.append(patient)
        except FileNotFoundError:
            print("File does not exist")
        return patient_list

    @staticmethod
    def write_patient_records(patients_file: str, patients: list):
        try:
            with open(patients_file, 'w') as file:
                for patient in patients:
                    file.write(f"{str(patient)}\n")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def __str__(self):
        return (f'{self.full_name():^30}|{self.__age:^5}|{self.__mobile:^15}|'
                f'{self.__postcode:^10}|{self.__address:^15}|{", ".join(self.__symptoms):^40}|{self.get_doctor():^10}')
