import africastalking

class SMS:
    def __init__(self):
        # Set your app credentials
        
        self.username = "YOUR_USERNAME"
        self.api_key = "YOUR_API_KEY"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        recipients = ["+254713YYYZZZ", "+254733YYYZZZ"]

        # Set your message
        message = "I'm a lumberjack and it's ok, I sleep all night and I work all day";

        # Set your shortCode or senderId
        sender = "shortCode or senderId"

        # hit send.
        try:
            response = self.sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()