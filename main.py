# Importing the required modules
from admin import Admin
from doctor import Doctor
from patient import Patient

def main():
    # Initializing the actors
    admin = Admin('admin', '123', 'B1 1AB')  # username is 'admin', password is '123'
 
    # Initializing doctors
    doctors = [
        Doctor('John', 'Smith',  'Internal Med.'),
        Doctor('Jone', 'Smith',  'Pediatrics'),
        Doctor('Jone',  'Carlos', 'Cardiology')
    ]


    patients = [
        Patient('Sara',  'Smith', 20, '07012345678', 'B1 234', 'Kathmandu', 'Headache,Fever' ),
        Patient('Mike',  'Jones', 37, '07555551234', 'L2 2AB', 'Lalitpur' , 'Cough,Nausea'), 
        Patient('Daivid','Smith', 15, '07123456789', 'C1 ABC', 'Bhaktapur', 'Backpain,Vomiting'),
        Patient('Jone',  'Carlos',18, '07212345678', 'D1 ABC', 'Pokhara',   'Brain tumor')
    ]
    f = open("patients_file.txt", "r")
    check = f.read()
    f.close()
    if check:
        patients = Patient.read_patient_records("patients_file.txt")
    else:
        pass
    discharged_patients = []
    for patient in patients:
        if patient.get_doctor()!="None":
            doctor_name = patient.get_doctor()
            for doctor in doctors:
                if doctor.full_name() == doctor_name:
                    doctor.add_patient(patient)
                else:
                    pass
        else:
            pass


    while True:
        try:
            if admin.login():
                running = True 
                break
            else:
                print('Incorrect username or password.')
        except Exception as e:
            print(f"An error occurred during login: {e}")

    while running:
        try:
            # Print the menu
            print('\nChoose the operation:')
            print(' 1- Register/view/update/delete doctor')
            print(' 2- View/Discharge patients')
            print(' 3- View discharged patient')
            print(' 4- Group patients by family')
            print(' 5- Add patients')
            print(" 6- Add Symptoms")
            print(' 7- Assign doctor to a patient')
            print(" 8- Update admin details")
            print(" 9- Relocate a patient from one doctor to another")
            print(" 10- Request management report")
            print(" 11- Exit")

            # Get the option
            op = input('Please enter your choice: ')

            if op == '1':
                admin.doctor_management(doctors)

            elif op == '2':
                print('Choose the operation:')
                print(' 1- view patients')
                print(' 2- Discharge patients')
                opt = int(input('Option: '))
                if opt == 1:
                    admin.view_patient(patients)
                elif opt == 2:
                    admin.view_patient(patients)
                    admin.discharge(patients, discharged_patients)
                    

            elif op == '3':
                # 3 - View discharged patients
                admin.view_discharge(discharged_patients)

            elif op == '4':
                # Group patients by family
                admin.same_family(patients)

            elif op == '5':
                # Add patients
                admin.admit_patient(patients)

            elif op == '6':
                try:
                    admin.view(patients)
                    index = int(input("Enter index of patient: ")) - 1
                    if 0 <= index < len(patients):
                        print("What do you want to do? ")
                        print(" 1. Add symptoms to patient ")
                        print(" 2. View symptoms of patient ")
                        op1 = input("Enter your choice: ")
                        if op1 == '1':
                            print("Welcome to Symptoms addition window")
                            new_symptoms = input(f"Enter the symptoms that need to be added for {patients[index].get_first_name()}: ")
                            patients[index].add_symptoms(new_symptoms)
                            print("Successfully Added!")
                        elif op1 == '2':
                            print("Symptoms of the patient:")
                            patients[index].print_symptoms()
                        else:
                            print("Invalid input!")
                    else:
                        print("Invalid index. Please enter a valid index.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif op == '7':
                # Assign doctor to a patient
                admin.assign_doctor_to_patient(patients, doctors)
            elif op == '8':
                # Update admin details
                admin.update_details(admin)

            elif op == '9':
                # Relocate a patient from one doctor to another
                admin.relocate_doctor(patients, doctors)

            elif op == '10':
                # Request management report
                admin.get_management_report(doctors, patients)

            elif op == '11':
                # Quit
                print("Goodbye")
                Patient.write_patient_records("patients_file.txt", patients)
                running = False
            else:
                # The user did not enter an option that exists in the menu
                print('Invalid option. Try again')

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Index out of range. Please enter a valid option.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()