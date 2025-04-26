from textblob import TextBlob

print("👋 Welcome to the AI Mood Detector!")
name = input("What's your name? ")
print(f"Nice to meet you, {name}! Let's find out the sentiment of your sentences.")
print("Type 'exit' to quit.")
print()

while True:
    sentence = input("📝 Your sentence: ")
    if sentence.lower() == "exit":
        print(f"Goodbye, {name}! 👋")
        break
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        print("😊 Positive sentiment detected!")
        print()
    elif sentiment < 0:
        print("😞 Negative sentiment detected!")
        print()
    else:
        print("😐 Neutral sentiment detected!")
        print()
        