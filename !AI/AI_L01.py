print("Hello! I'm your friendly chatbot.")
name = input("What's your name? ")
print(f"\nNice to meet you, {name}!")

print()

feeling = input("How are you feeling today? ").lower()
if "good" in feeling or "great" in feeling:
    print("\nI'm glad to hear that!\n")
elif "bad" in feeling :
    print("I'm sorry to hear that, hope things will get better")
else:
    print("I see. Sometimes its hard to put feelings into word")

print()
hobby = input("What's your favorite hobby? ")
print(f"Wow, {hobby} sounds fun!")
print()

print(f"it was nice chatting with you, {name}. Goodbye")