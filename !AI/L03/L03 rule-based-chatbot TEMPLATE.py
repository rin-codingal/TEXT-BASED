import re
import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Function to greet the user
def greet_user():
    print(Fore. + "Hello! ")
    name = input(Fore. + "May I know your name? ")
    print(Fore. + f"Nice to meet you, {name}! ")
    return name

# Function to show help options
def show_help():
    print(Fore. + "\nI can assist you with the following:")
    print(Fore. + "- ")
    print(Fore. + "- Offer ")
    print(Fore. + "- ")
    print(Fore. + "Just ask me a question or type 'exit' to leave.\n")

# Function to process user input
def process_input(user_input):
    # Convert input to lowercase, remove leading/trailing spaces, and replace multiple spaces with one
    user_input = 
    user_input =   # Replace multiple spaces with a single space
    return user_input

# Function to provide travel recommendations
def provide_recommendations():
    print(Fore. + "TravelBot: Sure! Are you interested in beaches, mountains, or cities?")
    preference = input(Fore. + "You: ")
    preference = ()  # Normalize the input

    if preference in destinations:
        suggestion = random.(destinations[preference])
        print(Fore. + f"TravelBot: How about visiting {}?")
        print(Fore.CYN + "TravelBot:  (yes/no)")
        response = input(Fore.YELLOW + "You: ").strip().lower()

        if response == "yes":
            print(f"{Fore.} TravelBot: Great!  {suggestion}!")
        elif response == "no":
            print(f"{Fore.}TravelBot: No worries! Let's find another place.")
            provide_recommendations()  # Recur to suggest another destination
        else:
            print(f"{Fore.}TravelBot: I didn't catch that. Let's start over.")
            provide_recommendations()  # Recur to handle unexpected input
    else:
        print(f"{Fore.}TravelBot: Sorry, I don't have recommendations for that preference.")

    # Show the help options again
    show_help()

# Function to offer packing tips
def offer_packing_tips():
    print(f"{Fore.} TravelBot: Where are you traveling to?")
    user_dest = input(f"{Fore.}You: ")
    user_dest = (user_dest)  # Normalize the input

    print(f"{Fore.}TravelBot: How many days will you be staying?")
    days = input(f"{Fore.YELLOW}You: ")

    print(f"{Fore.}TravelBot: Packing tips for {days} days in {user_dest}:")
    print(f"{Fore.}- Pack versatile clothing items.")
    print(f"{Fore.}- ")
    print(f"{Fore.}- ")

# Function to tell a joke
def tell_joke():
    

# Main chat function
def chat():
    name = greet_user()
    show_help()
    while True:
        user_input = input(f"{Fore.}{name}: ")
        processed_input = process_input(user_input)
        
        if "" in processed_input or "" in processed_input:
            provide_recommendations()
        elif "" in processed_input or "" in processed_input:
            offer_packing_tips()
        elif "" in processed_input or "" in processed_input:
            tell_joke()
        elif "" in processed_input:
            show_help()
        elif "" in processed_input or "" in processed_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore. + "TravelBot: I'm sorry, I didn't quite catch that. Could you please rephrase?")

# Start the chatbot
if __name__ == "__main__":
    chat()
