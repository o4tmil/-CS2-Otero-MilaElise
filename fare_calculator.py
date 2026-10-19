# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")

#validate customer name
if name.strip() == "":
    print("Invalid name. Please try again:")
    name = input("Enter passenger name.")

distance = float(input("Enter distance (km): "))

#validate distance
if distance <= 0:
    print("Invalid distance. Please try again")
    distance = float(input("Enter distance (km):"))

passengers = int(input("Enter number of passengers: "))

#validate number of passengers
if passengers < 0:
    print("Invalid number of passengers. Please try again.")
    passengers = int(input("Enter number of passengers."))


    
total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
