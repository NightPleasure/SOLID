from abc import ABC, abstractmethod


class IMessageSender(ABC):
    @abstractmethod
    def send_message(self, message):
        pass


class IMessageReceiver(ABC):
    @abstractmethod
    def receive_message(self):
        pass


class EmailSender(IMessageSender):
    def send_message(self, message):
        print(f"Sending email message: {message}")


class EmailReceiver(IMessageReceiver):
    def receive_message(self):
        message = "Example email message"
        print(f"Received email message: {message}")
        return message


class SMSsender(IMessageSender):
    def send_message(self, message):
        print(f"Sending SMS message: {message}")


class SMSreceiver(IMessageReceiver):
    def receive_message(self):
        message = "Example SMS message"
        print(f"Received SMS message: {message}")
        return message


class MessageService:
    def __init__(self, sender: IMessageSender, receiver: IMessageReceiver):
        self.sender = sender
        self.receiver = receiver

    def send_message(self, message):
        self.sender.send_message(message)

    def receive_message(self):
        self.receiver.receive_message()


email_sender = EmailSender()
email_receiver = EmailReceiver()
sms_sender = SMSsender()
sms_receiver = SMSreceiver()

email_service = MessageService(email_sender, email_receiver)
sms_service = MessageService(sms_sender, sms_receiver)

email_service.send_message("Hello, this is an email message")
email_service.receive_message()

sms_service.send_message("Hello, this is an SMS message")
sms_service.receive_message()
