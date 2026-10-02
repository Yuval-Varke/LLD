from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, to:str, title:str, body:str):
        pass


class EmailNotificationService(NotificationService):
    def send(self, to:str, title:str, body:str):
        print("\nSending Email through EmailNotificationService")
        print(f"To = {to}")
        print(f"Title = {title}")
        print(f"Body = {body}")





class SendGridEmailService:
    def send_email(self, recipient:str, subject:str, content:str):
        print("\nSending Email through SendGridEmailService")
        print(f"Recipient = {recipient}")
        print(f"Subject = {subject}")
        print(f"Content = {content}")


class SendGridAdapter(NotificationService):
    def __init__(self,send_grid_service : SendGridEmailService):
        self.__send_grid_service = send_grid_service

    def send(self, to:str, title:str, body:str):
        self.__send_grid_service.send_email(to,title,body)




class OrderService:
    def __init__(self,email_service : NotificationService):
        self.__email_service = email_service

    def create_order(self):
        self.__email_service.send(
            "yuval@gmail.com","New Order","Order has been placed and delivery available !"
        )



# email_ns = EmailNotificationService()
# os = OrderService(email_ns)
# os.create_order()

send_grid_es = SendGridEmailService()
send_grid_adp = SendGridAdapter(send_grid_es)
os = OrderService(send_grid_adp)
os.create_order()