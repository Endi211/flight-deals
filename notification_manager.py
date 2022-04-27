from twilio.rest import Client
import smtplib


TWILIO_SID = "AC19bd98dc136b21b79fa84306f0af5b2b"
TWILIO_AUTH_TOKEN = "afd50edddd7a1c775783454ac460ef0c"
TWILIO_VIRTUAL_NUMBER = '+13862304120'
TWILIO_VERIFIED_NUMBER = '+355684306977'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("EMAIL_PROVIDER_SMTP_ADDRESS") as connection:
            connection.starttls()
            connection.login("MY_EMAIL, MY_PASSWORD")
            for email in emails:
                connection.sendmail(
                    from_addr="MY_EMAIL",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )