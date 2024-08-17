# Automatic Health Monitoring System

import time
import random
from datetime import datetime, timedelta

# Define a class for the Health Monitoring System
class HealthMonitoringSystem:
    def __init__(self, patient_name, patient_age):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_data = []

    def generate_random_past_datetime(self):
        """Generate a random past date and time within the last 30 days."""
        days_ago = random.randint(0, 30)
        random_date = datetime.now() - timedelta(days=days_ago)
        random_time = timedelta(
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )
        return random_date + random_time

    def update_health_data(self):
        """Simulate health data collection for the patient."""
        # Simulate health data
        heart_rate = random.randint(60, 100)  # beats per minute
        blood_pressure = f"{random.randint(90, 120)}/{random.randint(60, 80)}"  # mmHg
        glucose_level = random.randint(70, 120)  # mg/dL
        
        # Store the report with a random past date and time
        report = {
            'heart_rate': heart_rate,
            'blood_pressure': blood_pressure,
            'glucose_level': glucose_level,
            'timestamp': self.generate_random_past_datetime().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.patient_data.append(report)

    def display_report(self):
        """Display the health report for the patient."""
        print(f"\nHealth Report for {self.patient_name} (Age: {self.patient_age})")
        for report in self.patient_data:
            print(f"Timestamp: {report['timestamp']}, "
                  f"Heart Rate: {report['heart_rate']} bpm, "
                  f"Blood Pressure: {report['blood_pressure']} mmHg, "
                  f"Glucose Level: {report['glucose_level']} mg/dL")
            print("---")

# Main Program
if __name__ == "__main__":
    # Get patient details from user
    patient_name = input("Enter patient's name: ")
    patient_age = input("Enter patient's age: ")

    print("\nStarting Health Monitoring...\n")
    
    # Create an instance of the Health Monitoring System for the specific patient
    system = HealthMonitoringSystem(patient_name, patient_age)
    
    # Simulate regular updates
    for _ in range(12):  # You can change the range to get more reports
        system.update_health_data()
        time.sleep(1)  # Simulate time interval between updates
    
    # Display the health reports
    system.display_report()

    print("Monitoring Completed.")
