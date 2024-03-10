class User:
    def __init__(self,name,contact) -> None:
        self.name = name
        self.contact = contact

class Event:
    def __init__(self,name,detail=None,type=None,owner=None) -> None:
        self.name = name
        self.detail = detail
        self.type = type
        self.owner = owner

class TicketBooking:
    def __init__(self,event,booking_time,customer,price) -> None:
        self.event = event
        self.booking_time = booking_time
        self.customer = customer
        self.price = price


