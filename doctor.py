class Doctor:


    def __init__(self, first_name: str, surname: str, speciality: str):
       
        self._first_name = first_name
        self._surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = {}

    def get_first_name(self):
        return self._first_name

    def get_surname(self):
        return self._surname
    
    def set_first_name(self, new_first_name):
        self._first_name = new_first_name

    def set_surname(self, new_surname):
        self._surname = new_surname


    def full_name(self):
        return f"{self._first_name} {self._surname}"

    def get_speciality(self) -> str:
        return self.__speciality

    def set_speciality(self, new_speciality: str):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_total_patients(self) -> int:
        return len(self.__patients)

    def get_patients(self) -> list:
        return self.__patients

    def add_appointment(self, appointment_date):
        month_year = appointment_date.strftime("%B %Y")
        if month_year not in self.__appointments:
            self.__appointments[month_year] = 1
        else:
            self.__appointments[month_year] += 1

    def get_appointments(self):
        return self.__appointments

    def __str__(self) -> str:
        return f'{self.full_name():^30}|{self.__speciality:^15}'
