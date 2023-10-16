import csv
import argparse
from geopy.distance import geodesic



csv_file_name = "Mobile_Food_Facility_Permit.csv"


# List all food trucks in the CSV file
def list_food_trucks(file_path):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            print("Applicant:", row['Applicant'])
            print("Food Items:", row['FoodItems'])
            print("Address:", row["Address"])
            print("Location:", row['Location'])
            print("=" * 30)



# Function to search for specific types of food trucks
def search_food_trucks(file_path, food_type):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        found_trucks = []
        for row in csvreader:
            if food_type.lower() in row['FoodItems'].lower():
                found_trucks.append(row)
            elif food_type.lower() in row["Applicant"].lower():
                found_trucks.append(row)

        if found_trucks:
            print(f"Food Trucks serving {food_type}:")
            for truck in found_trucks:
                print("Applicant:", truck['Applicant'])
                print("Food Items:", row['FoodItems'])
                print("Location:", truck['Location'])
                print("=" * 30)
        else:
            print(f"No food trucks found serving {food_type}.")


# Function to provide information about food trucks in a specific address
def location_info(file_path, location):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        found_trucks = []
        for row in csvreader:
            if location.lower() in row['Address'].lower():
                found_trucks.append(row)

        if found_trucks:
            print(f"Food Trucks in {location}:")
            for truck in found_trucks:
                print("Applicant:", truck['Applicant'])
                print("Food Items:", truck['FoodItems'])
                print("Address:", truck["Address"])
                print("=" * 30)
        else:
            print(f"No food trucks found in {location}.")



# Function to calculate the distance between two coordinates
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).miles

# Function to find and display nearby food trucks
def find_nearby_food_trucks(file_path, location, max_distance):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        nearby_trucks = []
        for row in csvreader:
            truck_location = (float(row['Latitude']), float(row['Longitude']))
            distance = calculate_distance(location, truck_location)
            if distance <= max_distance:
                nearby_trucks.append(row)

        if nearby_trucks:
            print(f"Nearby Food Trucks within {max_distance} meters:")
            for truck in nearby_trucks:
                truck_location = (float(truck['Latitude']), float(truck['Longitude']))
                distance = calculate_distance(location, truck_location)
                print("Applicant:", truck['Applicant'])
                print("Food Items:", truck["FoodItems"])
                print("Address:", truck["Address"])
                print("Location:", truck['Location'])
                print("Distance:", distance, "meters")
                print("=" * 30)
        else:
            print(f"No food trucks found within {max_distance} meters of the specified location.")





# Main function to handle user interactions
def main():
    while True:
        print("\nAvailable commands:")
        print("1. list - List all food trucks")
        print("2. search - Search for specific food trucks")
        print("3. address - Get information about food trucks in an address")
        print("4. distance - Calculate the distance to food trucks")
        print("5. nearby - Find nearby food trucks")
        print("6. exit - Exit the program")
        
        user_input = input("Enter a command: ").strip()

        if user_input == "list":
            list_food_trucks(csv_file_name)
        elif user_input == "search":
            food_type = input("Enter the type of food to search for: ").strip()
            search_food_trucks(csv_file_name, food_type)
        elif user_input == "address":
            location = input("Enter the address to search for (For example: California): ").strip()
            location_info(csv_file_name, location)
        elif user_input == "distance":
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            max_distance = float(input("Enter maximum distance (meters): "))
            # Calculate the distance from a specified location to all food trucks
            if latitude is not None and longitude is not None:
                user_location = (latitude, longitude) # Specify the user's location (latitude, longitude)
                with open(csv_file_name, 'r') as csvfile:
                    csvreader = csv.DictReader(csvfile)
                    nearby_trucks = []
                    for row in csvreader:
                        truck_location = (float(row['Latitude']), float(row['Longitude']))
                        distance = calculate_distance(user_location, truck_location)
                        # Display only the truck and its distance if it is within the specified distance
                        if distance <= max_distance:
                            print("Applicant:", row['Applicant'])
                            print("Food Items:", row["FoodItems"])
                            print("Address:", row["Address"])
                            print("Location:", row['Location'])
                            print("Distance:", distance, "meters")
                            print("=" * 30)
        elif user_input == "nearby":
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            max_distance = float(input("Enter maximum distance (meters): "))
            user_location = (latitude, longitude)
            find_nearby_food_trucks(csv_file_name, user_location, max_distance)
        elif user_input == "exit":
            break
        else:
            print("Invalid command. Please choose a valid command from the docs.")

if __name__ == "__main__":
    main()