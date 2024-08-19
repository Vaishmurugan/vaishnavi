import time

# Twilio credentials (for simulation, credentials are not used here)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
TO_PHONE_NUMBER = 'recipient_phone_number'

def send_sms(message):
    # Simulating sending an SMS
    print(f"SMS sent to {TO_PHONE_NUMBER}: {message}")

def check_health_from_file():
    try:
        # Simulate reading from a file
        data = [
            "HeartRate: 105",
            "BloodPressure: 120/80"
        ]
        # Example of health condition check
        heart_rate = int(data[0].split(': ')[1])
        # Simulate a health issue if heart rate is above 100
        if heart_rate > 100:
            return True
    except FileNotFoundError:
        print("Health data file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False

def simulate_image_capture():
    # Simulate capturing an image from a webcam
    filename = 'simulated_image.txt'
    # Create a dummy file to simulate image capture
    with open(filename, 'w') as file:
        file.write("This is a simulated image file.")
    print(f"Simulated image saved as {filename}")
    return filename

def main():
    while True:
        # Check health condition from the file
        if check_health_from_file():
            # Simulate image capture
            simulate_image_capture()
            send_sms("Alert: High heart rate detected! Simulated image captured.")
            print("Health issue detected. SMS sent.")
            time.sleep(10)  # Delay to avoid sending multiple messages
        
        # Exit condition (for demo purposes, run indefinitely or add a condition to exit)
        user_input = input("Enter 'exit' to stop or press Enter to continue: ")
        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    main()

