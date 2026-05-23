# Booking class + ID generator
import secrets
import string
import time
from datetime import datetime
from models.passenger import Passenger
from models.flight import Flight

class Booking:
        def __init__(self, passenger, flight):
            self.booking_id = self.unique_ticket_id()

            self.passenger = passenger

            self.flight = flight

            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.status = "CONFIRMED"

        def unique_ticket_id(self,prefix="TKT", length=8):
            chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
            random_part = ''.join(secrets.choice(chars) for _ in range(length))
            date_part = datetime.now().strftime("%y%m%d")
            return f"{prefix}-{date_part}-{random_part}"

        def booking_summary(self):


                print(f"""
                ================================
                BOOKING CONFIRMED
                ================================
                
                Booking ID : {self.booking_id}
                Passenger  : {self.passenger.name}
                Flight     : {self.flight.flight_number}
                Route      : {self.flight.origin} -> {self.flight.destination}
                Status     : {self.status}
                Booked At  : {self.created_at}
                
                ================================
    """)


        def to_dict(self):
            return {

                "booking_id": self.booking_id,

                "passenger_name": self.passenger.name,

                "passenger_email": self.passenger.email,

                "passenger_phone": self.passenger.phone,

                "flight_number": self.flight.flight_number,

                "airline": self.flight.airline,

                "origin": self.flight.origin,

                "destination": self.flight.destination,

                "status": self.status,

                "created_at": self.created_at
            }
