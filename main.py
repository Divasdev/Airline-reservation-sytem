import requests
import resend
import json
import os
from dotenv import load_dotenv
from services.file_handler import initialize_booking_file
from services.flight_api import FlightAPI
from models.passenger import Passenger
from models.booking import Booking
load_dotenv()
flights_api=FlightAPI()

load_dotenv()

initialize_booking_file()

def cli_menu():
    print("""
╔══════════════════════════════════════╗
║   ✈️  FLIGHT RESERVATION SYSTEM      ║
║           Powered by AviationStack   ║
║                   & Resend API       ║
╠══════════════════════════════════════╣
║  1. Search & Book a Flight           ║
║  2. Cancel a Booking                 ║
║  3. View My Bookings                 ║
║  4. Exit                             ║
╚══════════════════════════════════════╝
""")

    choice = input("Enter your choice (1-4): ")

    return choice

chose=cli_menu()


def search_and_book():

    origin = input("🛫 From Airport (IATA Code): ").upper()
    destination = input("🛬 To Airport (IATA Code): ").upper()


    raw_flights=flights_api.get_flights(origin,destination)

    parsed_flights=flights_api.parse_flights(raw_flights)

    visible_flights = 10

    if parsed_flights:

        while True:

            print("\nAvailable Flights\n")

            print("=" * 78)

            print(
                f"{'No':<4}"
                f"{'Flight':<12}"
                f"{'Airline':<28}"
                f"{'From':<8}"
                f"{'To':<8}"
                f"{'Status':<12}"
            )

            print("=" * 78)

            for index, flight in enumerate(parsed_flights[:visible_flights], start=1):
                flight.display(index)

            print("=" * 78)

            if visible_flights < len(parsed_flights):
                more_choice = input("Do you want to see more flights? (yes/no): ").lower()

                if more_choice == "yes":
                    visible_flights += 10
                    continue

            break

        while True:

            passenger_name = input("Enter Your Name: ").upper()
            passenger_email = input("Enter Your Email: ")
            passenger_phone = input("Enter Your Phone No.: ")

            passenger_flight_choice = input("Enter Your Preferred Flight Number: ")
            if not passenger_flight_choice.isdigit():
                print("Invalid flight number choice!")
                continue

            passenger_flight_choice = int(passenger_flight_choice)

            if passenger_flight_choice < 1 or passenger_flight_choice > len(parsed_flights[:visible_flights]):
                print("Please choose a valid available flight number!")
                continue

            passenger = Passenger(
                passenger_name,
                passenger_email,
                passenger_phone,

            )

            if passenger.validate():
                print("Passenger details validated!")
                selected_flight=parsed_flights[passenger_flight_choice-1]
                print(f"You selected flight: {selected_flight.flight_number}")

                booking = Booking(passenger, selected_flight)

                booking.booking_summary()

                break

            else:
                print("Invalid details. Please try again.")

    else:
        print("No flights available!")


if chose=="1":
  search_and_book()

elif chose=="2":
  # cancel_booking()
  pass

elif chose == "3":
  # view_bookings()
  pass
