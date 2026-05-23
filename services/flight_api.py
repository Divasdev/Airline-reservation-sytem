# search_flights()
# get_flight_details()
import os
import requests
import json
from dotenv import load_dotenv
from models.flight import Flight

load_dotenv()



class FlightAPI:
    def __init__(self):
        self.api=os.getenv("AVIATION_STACK_API_KEY")
        self.url="https://api.aviationstack.com/v1/flights"



    def get_flights(self,dept_iata,arr_iata):
        params={
            "access_key": self.api,
            "dep_iata":dept_iata,
            "arr_iata":arr_iata
        }

        # #This is for dev mode
        # with open("data/flights.json","r") as datafile:
        #     data=json.load(datafile)
        #
        # flights_list = data["data"]

        # this for the live api call
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()

            new_data=response.json()

            if "data" not in new_data:
                print("No flight data found.")
                return []

            with open("data/flights.json","w") as df:
                json.dump(new_data, df ,indent=4)

            flights_list=new_data["data"]

            return flights_list
        except requests.exceptions.RequestException as e:
            print(f"API Response Error:,{e}")
        except requests.JSONDecodeError:
            print("Invalid JSON response  from API")
        except IOError:
            print("Error writing to flights.json")
        except Exception as e:
            print(f"Unexpected Error: {e}")


    def parse_flights(self,flights_list):
        parse_flights=[]
        for flight in flights_list:
            flight_number = flight["flight"]["iata"]
            airline_name = flight["airline"]["name"]

            departure_code = flight["departure"]["iata"]
            departure_time = flight["departure"]["scheduled"]

            arrival_code = flight["arrival"]["iata"]
            arrival_time = flight["arrival"]["scheduled"]

            status = flight["flight_status"]
            flight_object = Flight(
                flight_number,
                airline_name,
                departure_code,  # origin
                arrival_code,  # destination
                departure_time,  # departure
                arrival_time,  # arrival
                status
            )
            parse_flights.append(flight_object)
        return parse_flights




































