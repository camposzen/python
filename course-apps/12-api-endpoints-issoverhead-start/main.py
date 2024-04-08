import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 47.376888  # Your latitude
MY_LONG = 8.541694  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def send_msg():
    my_email = "202.droidzen@gmail.com"
    my_password = "uliffeqsxrtegsii"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="202.droidzen@gmail.com",
            msg=f"Subject:Look up!\n\nThe ISS is above you in the sky."
        )


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (iss_latitude - 5) <= MY_LAT <= (iss_latitude + 5) and \
        (iss_longitude - 5) <= MY_LONG <= (iss_longitude + 5)


def is_dark():
    # Your position is within +5 or -5 degrees of the ISS position.
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(f"hour sunrise: {sunrise}")
    print(f"hour sunset: {sunset}")

    time_now = datetime.now()
    time_now = time_now.hour
    print(f"hour now: {time_now}")

    return time_now >= sunset


email_sent = False
while not email_sent:
    # If the ISS is close to my current position
    if is_iss_overhead():
        print("ISS is above")
        # and it is currently dark
        if is_dark:
            print("It's dark")
            # Then email to tell me to look up.
            send_msg()
            email_sent = True

        else:
            print("Still bright")
    else:
        print("ISS is far")

    time.sleep(60)

# BONUS: run the code every 60 seconds.
