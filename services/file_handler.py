# initialize_booking_file()
# save_booking()
# load_bookings()
# cancel_booking()

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









