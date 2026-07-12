# ================================
# MY TRAVEL TICKET COUNTER
# ================================
 
# PART 1 - TYPES OF DATA
 
passenger_name = "Nurinn"        # str - text
destination = "Derawan"             # str - text
ticket_price = 850.50           # float - decimal number
number_of_tickets = 3           # int - whole number
is_available = True             # bool - True or False
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: Rs", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
 
# PART 2 - ARITHMETIC OPERATORS
 
total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount
 
print("\nTotal Cost: IDR", total_cost)
print("Discount: IDR", discount)
print("Final Cost: IDR", final_cost)
 
print("Double Ticket Price: IDR", ticket_price * 2)
print("Ticket Price After IDR 50 Increase: IDR", ticket_price + 50)
print("Half Ticket Price: IDR", ticket_price / 2)
 
# PART 3 - COMPARISON OPERATORS
 
print("\nIs ticket price under IDR 1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination Derawan?", destination == "Derawan")
print("Is final cost more than IDR 2000?", final_cost > 2000)
 
# PART 4 - STRING OPERATIONS
 
travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))
 
# PART 5 - SWAPPING VALUES
 
morning_ticket_price = 700
evening_ticket_price = 900
 
print("\nBefore Swapping:")
print("Morning Ticket Price: IDR", morning_ticket_price)
print("Evening Ticket Price: IDR", evening_ticket_price)
 
morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price
 
print("\nAfter Swapping:")
print("Morning Ticket Price: IDR", morning_ticket_price)
print("Evening Ticket Price: IDR", evening_ticket_price)
 
# FINAL SUMMARY
 
print("\n================================")
print("TRAVEL TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: IDR", final_cost)
print("Booking Confirmed?", is_available)
