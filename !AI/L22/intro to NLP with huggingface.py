from transformers import pipeline

def sentiment_analyzer(texts):
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    if isinstance(texts, str) :
        texts = [texts] #convert to list because sentiment analyzer doesn't support normal string only list
    
    results = sentiment_pipeline(texts)
    #return [{'text': text, 'sentiment': result['label'], 'score':result['score']} for text, result in zip(texts, results)]

    return results

def analyze_text_input():
    text = input("Enter a sentence or multiple sentences (separated by '|)")
    texts = text.split('|')
    sentiments = sentiment_analyzer(texts)

    for i, sentiment in enumerate(sentiments):
        print(f"sentences {i+1}: {texts[i].strip()}")
        print(f"sentiment: {sentiment['label']}, confidence: {sentiment['score']:.4f}\n")

def analyze_text_file():
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            texts = file.readlines()
        texts = [line.strip() for line in texts if line.strip()]
        sentiments = sentiment_analyzer(texts)

        for i, sentiment in enumerate(sentiments):
            print(f"line {i+1}: {texts[i]}")
            print(f"sentiment: {sentiment['label']}, confidence: {sentiment['score']:.4f}\n")
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again")

choice = input("Choose input method (1) manual text input or (2) text file: ")

if choice == "1":
    analyze_text_input()
elif choice == "2":
    analyze_text_file()
else:
    print("invalid")