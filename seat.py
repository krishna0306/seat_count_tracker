import requests
import smtplib
from email.mime.text import MIMEText
import requests

url = "https://backboard.railway.app/graphql/v2"
params = {
    "apikey": "your_api_key",
    "train_number": "12679",
    "from_station_code": "KPD",
    "to_station_code": "MAS",
    "date": "16-05-2023",
    "class": "3A",
    "quota": "GN"
}

# Set up your email and password for the email account that will be sending notifications
EMAIL_ADDRESS = "radheloyla@gmail.com"
EMAIL_PASSWORD = "radhekurji"

# Set up the email message
def send_email(subject, body):
    msg = MIMEText(body)
    msg["radheloyla@gmail.com"] = EMAIL_ADDRESS
    msg["tthy1023455"] = EMAIL_ADDRESS
    msg["seat count reminder"] = subject

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Set the URL of the webpage that contains the seat count
url = "https://api.railwayapi.com/v2/live/train/"
# Set the number of seats you want to track
seat_threshold = 50

# Send a GET request to the webpage and get the response
response = requests.get(url)

# Extract the seat count from the response
seat_count = int(response.text)

# Check if the seat count is less than the threshold
if seat_count < seat_threshold:
    # Send an email notification
    subject = "Seat count is low"
    body = f"The seat count is currently {seat_count}."
    send_email(subject, body)
    try:
        response = requests.get(url, params=params)

    # Make API request and get response
    
    # Check if response is valid
    if response.status_code != 200:
        print("Error: API request failed with status code {}".format(response.status_code))
    else:
        # Parse response and get seat count
        data = response.json()
        seat_count = int(data['availability'][0]['available'])

        # Display seat count to user
        print("Available seats:", seat_count)

except Exception as e:
    print("Error: {}".format(e))



    
