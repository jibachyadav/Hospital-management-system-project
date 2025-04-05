from doctor import Doctor
from patient import Patient
import matplotlib.pyplot as plt
import datetime


class Admin:
    def __init__(self, username, password, address='None'):
        self.__username = username
        self.__password = password
        self.__address = address

    def view(self,a_list):
        for index, item in enumerate(a_list):
            print(f'{index+1:^5}|{item}')

    def find_index(self, index, items):
        try:
            index = int(index)
            if index in range(len(items)):
                return True
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid index.")

        return False 
    
    def login(self):
        """Admin login."""
        print("-----Login-----")
        username = input('Enter the username: ')
        password = input('Enter the password: ')
        return self.__username == username and self.__password == password


    def get_doctor_details(self):
        """Get doctor details from input."""
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """Manage doctor-related operations."""
        print("-----Doctor Management-----")
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        
        op = input('Which operation do you want: ')

        if op == '1':
            print("-----Register-----")
            first_name, surname, speciality = self.get_doctor_details()
            name_exists = any(first_name == doctor.get_first_name() and surname == doctor.get_surname() for doctor in doctors)
            if name_exists:
                print('Name already exists.')
            else:
                doctors.append(Doctor(first_name, surname, speciality))
                print('Doctor registered.')

        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    if self.find_index(index, doctors):
                        break
                    else:
                        print("Doctor not found")
                except ValueError:
                    print('The ID entered is incorrect')

            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            try:
                op = int(input('Input: '))
                if op == 1:
                    new_first_name = input("Enter first name: ")
                    doctors[index].set_first_name(new_first_name)
                    print(f"{new_first_name} is updated succesfully!!!")
                elif op == 2:
                    new_surname = input("Enter surname: ")
                    doctors[index].set_surname(new_surname)
                elif op == 3:
                    speciality = input("Enter speciality: ")
                    doctors[index].set_speciality(speciality)
                else:
                    print("Error: Invalid option")
            except ValueError:
                print("Please enter a valid number.")

        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
                if self.find_index(doctor_index, doctors):
                    del doctors[doctor_index]
                    print("Doctor deleted.")
                else:
                    print('The ID entered is incorrect')
            except ValueError:
                print('The ID entered is incorrect')

        else:
            print('Invalid operation chosen. Check your input!')

    def view_patient(self, patients):
        """View list of patients."""
        print("-----View Patients-----")
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |    Address    |                Symptoms                ')
        print(f'{"ID":^5}|{"Full Name":^30}|{"Age":^5}|{"Mobile":^15}|'
                f'{"Postcode":^10}|{"Address":^15}|{"Symptoms":^40}|{"Doctor Name":^10}')
        self.view(patients)

    def discharge(self, patients, discharged_patients):
        """Discharge a patient."""
        print("-----Discharge Patient-----")
        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if self.find_index(patient_index, patients):
                discharged_patients.append(patients[patient_index])
                print(f"{patients[patient_index].full_name()} has been discharged.")
                del patients[patient_index]
                Patient.write_patient_records('patients_file.txt', patients)
            else:
                print('The ID entered is incorrect')
        except ValueError:
            print('Invalid patient ID.')

    def view_discharge(self, discharged_patients):
        """View list of discharged patients."""
        print("-----Discharged Patients-----")
        print(f'{"ID":^5}|{"Full Name":^30}|{"Age":^5}|{"Mobile":^15}|'
                f'{"Postcode":^10}|{"Address":^15}|{"Symptoms":^40}|{"Doctor name":^10}')
        self.view(discharged_patients)

    def same_family(self, patients):
        """Group patients by family (surname)."""
        same_family = {}
        for patient in patients:
            patient_surname = patient.get_surname()
            same_family.setdefault(patient_surname, []).append(patient)

        for family_name, family_members in same_family.items():
            print(f"Family Name: {family_name}")
            for patient in family_members:
                print(patient)

    def admit_patient(self, patients):
        """Admit a new patient."""
        try:
            f_name = input("Enter patient first name: ")
            l_name = input("Enter patient surname: ")
            age = int(input("Enter age: "))
            mobile = input("Enter the mobile number: ")
            postcode = input("Enter the postcode: ")
            symptoms = input("Enter the symptoms: ")
            address = input("Enter the address: ")
            patients.append(Patient(f_name, l_name, age, mobile, postcode, address, symptoms))
            Patient.write_patient_records('patients_file.txt', patients) 
            self.view(patients)
        except Exception as e:
            print(f"An error occurred while admitting the patient: {e}")

    def assign_doctor_to_patient(self, patients, doctors):
        """Assign a doctor to a patient."""
        print("-----Assign-----")
        print("-----Patients-----")
        print(f'{"ID":^5}|{"Full Name":^30}|{"Age":^5}|{"Mobile":^15}|'
                f'{"Postcode":^10}|{"Address":^15}|{"Symptoms":^40}|{"Doctor Name":^10}')
        self.view(patients)
        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if not self.find_index(patient_index, patients):
                print('The ID entered was not found.')
                return
        except ValueError:
            print('The ID entered is incorrect')
            return
        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()
        print('ID |          Full Name           |  Speciality')
        self.view(doctors)
        try:
            doctor_index = int(input('Please enter the doctor ID: ')) - 1
            if self.find_index(doctor_index, doctors):
                # patients[patient_index].link(doctors[doctor_index].full_name())
                appointment_month = input("\nEnter the appointment month (e.g., January): ")
                appointment_year = input("Enter the appointment year (e.g., 2025): ")
                appointment_date = datetime.datetime(int(appointment_year), datetime.datetime.strptime(appointment_month, "%B").month, 1)
                patients[patient_index].link(doctors[doctor_index].full_name(), appointment_date)
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                doctors[doctor_index].add_appointment(appointment_date)
                print('The patient is now assigned to the doctor.')
            else:
                print('The ID entered was not found.')
        except ValueError:
            print('The ID entered is incorrect')

    def update_details(self,admin):
        """Update admin details."""
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        try:
            op = int(input('Input: '))
            if op == 1:
                self.__username = input("Enter new username: ")
                print(f"{self.__username} as username updated")
            elif op == 2:
                new_password = input('Enter the new password: ')
                if new_password == input('Enter the new password again: '):
                    self.__password = new_password
                    print("Password Changed!")
            elif op == 3:
                self.__address = input("Enter new address: ")
                print(f"{self.__address} as new address updated")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid input.")


    def relocate_doctor(self, patients, doctors):
        """Relocate doctor for a patient."""
        print("-----Relocate Doctor-----")
        print("-----List of Patients-----")
        self.view(patients)
        if patients:
            try:
                patient_index = int(input('Enter the ID of the patient to relocate the doctor from: ')) - 1
                if self.find_index(patient_index, patients):
                    print("-----List of Doctors-----")
                    self.view(doctors)
                    new_doctor_index = int(input('Enter the ID of the new doctor: ')) - 1
                    if self.find_index(new_doctor_index, doctors):
                        old_doctor_full_name = patients[patient_index].get_doctor()
                        # patients[patient_index].link(doctors[new_doctor_index].full_name())
                        appointment_month = input("\nEnter the appointment month (e.g., January): ")
                        appointment_year = input("Enter the appointment year (e.g., 2025): ")
                        appointment_date = datetime.datetime(int(appointment_year), datetime.datetime.strptime(appointment_month, "%B").month, 1)
                        patients[patient_index].link(doctors[new_doctor_index].full_name(), appointment_date)
                        doctors[new_doctor_index].add_patient(patients[patient_index])
                        print(f"Successfully relocated {old_doctor_full_name} to {doctors[new_doctor_index].full_name()}.")
                        Patient.write_patient_records("patients_file.txt",patients) 
                    else:
                        print('Invalid new doctor ID. Check your input.')
                else:
                    print('Invalid patient ID. Check your input.')
            except ValueError:
                print('Invalid input for patient or new doctor ID. Please enter a valid integer.')
        else:
            print('No patients available for relocation.')
        
    def get_management_report(self, doctors, patients):
        """Generate management reports."""
        print("-----Management Reports-----")
        print('Choose the operation:')
        print(' 1 - Total number of doctors in the system')
        print(' 2 - Total number of patients per doctors')
        print(' 3 - Total number of appointments per month per doctor')
        print(' 4 - Total number of patients based on the illness type.')
        op = input('Choose an option: ')
        try:
            if op == '1':
                total_doctors = len(doctors)
                print(f"The total number of doctors: {len(doctors)}")
                plt.bar('Doctors', total_doctors)
                plt.xlabel('')
                plt.ylabel('Count')
                plt.title('Total number of doctors in the system')
                plt.show()
                
            elif op == '2':
                for doctor in doctors:
                    total_patients = doctor.get_total_patients()
                    print(f"{doctor.full_name()} has {total_patients} patients")
                doctor_names = [doctor.full_name() for doctor in doctors]
                total_patients = [doctor.get_total_patients() for doctor in doctors]
                plt.bar(doctor_names, total_patients)
                plt.xlabel('Doctors')
                plt.ylabel('Total Patients')
                plt.title('Total patients per doctor')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif op == '3':
                print("\nTotal number of appointments per month per doctor:")
                for doctor in doctors:
                    print(f"{doctor.full_name()}:")
                    assigned_patients = [patient for patient in patients if patient.get_doctor() == doctor.full_name()]
                    if assigned_patients:
                        appointments = doctor.get_appointments()
                        if not appointments:
                            print("   - 0 appointments")
                        else:
                            for month, count in appointments.items():
                                print(f"   - {month}: {count} appointments")
                    else:
                        print("   - 0 appointments")

            elif op == '4':
                symptom_counts = {}
                for patient in patients:
                    for symptom in patient.get_symptoms():
                        if symptom not in symptom_counts:
                            symptom_counts[symptom] = 1
                        else:
                            symptom_counts[symptom] += 1

                # Print the total number of patients with each symptom
                for symptom, total in symptom_counts.items():
                    print(f'The total number of patients with {symptom}: {total}')

                # Prepare data for visualization
                symptom_names = list(symptom_counts.keys())
                pt_wt_ssymp = list(symptom_counts.values())

                # Plot the data
                plt.figure(figsize=(10, 6))
                plt.bar(symptom_names, pt_wt_ssymp)
                plt.xlabel('Symptoms')
                plt.ylabel('Total Patients')
                plt.title('Total number of patients with each symptom')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.show()
        except Exception as e:
                print(e)

        
   