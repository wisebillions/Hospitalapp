# Importing necessary libraries
import datetime

# Defining the Hospital class
class Hospital:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.bookings = []

    # Defining the method to book an appointment
    def book_appointment(self, patient_name, appointment_date):
        if len(self.bookings) >= self.capacity:
            print("Sorry, all appointments are fully booked for the selected date.")
            return False

        for booking in self.bookings:
            if booking['date'] == appointment_date:
                print(f"Sorry, appointment already exists for {appointment_date}.")
                return False

        new_booking = {'patient_name': patient_name, 'date': appointment_date}
        self.bookings.append(new_booking)

        print(f"Appointment for {patient_name} on {appointment_date} has been booked successfully!")
        return True

    # Defining the method to show all appointments
    def show_appointments(self):
        print(f"Appointments for {self.name}:")
        for booking in self.bookings:
            print(f"{booking['patient_name']} on {booking['date']}")

# Defining the main function
def main():
    # Creating a new hospital
    reliance_hospital = Hospital("Reliance Infosystems Ltd", "Lagos", 50)

    # Booking appointments
    reliance_hospital.book_appointment("John Doe", datetime.date(2023, 5, 1))
    reliance_hospital.book_appointment("Jane Doe", datetime.date(2023, 5, 3))
    reliance_hospital.book_appointment("James Smith", datetime.date(2023, 5, 3))
    reliance_hospital.book_appointment("Mary Smith", datetime.date(2023, 5, 5))

    # Showing all appointments
    reliance_hospital.show_appointments()

# Calling the main function
if __name__ == '__main__':
    main()
