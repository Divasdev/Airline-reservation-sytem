# flight class


class Flight:
    def __init__(self, flight_number, airline, origin,
                 destination, departure, arrival, status):
        self.flight_number=flight_number
        self.airline=airline
        self.origin=origin
        self.destination=destination
        self.departure=departure
        self.arrival=arrival
        self.status=status

    def display(self, index):
        print(
            f"{index:<3}"
            f"{self.flight_number:<12}"
            f"{self.airline:<30}"
            f"{self.origin:<8}"
            f"{self.destination:<8}"
            f"{self.status:<12}"
        )

    def to_dict(self):

        return{
            "flight_number": self.flight_number,
            "airline": self.airline,
            "origin": self.origin,
            "destination": self.destination,
            "departure": self.departure,
            "arrival": self.arrival,
            "status": self.status

        }














