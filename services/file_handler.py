# initialize_booking_file()
# save_booking()
# load_bookings()
# cancel_booking()
from models.booking import Booking


import  json
import os
def initialize_booking_file():

    file_path="data/bookings.json"

    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"w") as file:
            json.dump([],file)

            print(f"Created {file_path} with and empty JSON list.")

    else:
        print(f"{file_path} already exist")

def save_booking(booking):

    file_path = "data/bookings.json"

    booking_data = booking.to_dict()

    with open(file_path, "r") as file:
        bookings = json.load(file)

    bookings.append(booking_data)

    with open(file_path, "w") as file:
        json.dump(bookings, file, indent=4)
    is_booked=True

    print("Booking saved successfully!")













