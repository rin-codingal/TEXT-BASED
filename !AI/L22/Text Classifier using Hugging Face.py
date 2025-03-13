import requests
#pip install huggingface_hub

# Hugging Face API endpoint for DistilBERT (sentiment analysis)
#api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased"

# Your Hugging Face API token (replace with your actual token)
headers = {
    #"Authorization": "Bearer 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"
    #"Authorization": "Bearer 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"
    #"Authorization": "Bearer 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"
    #"Authorization": "Bearer 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" # read
    
}

# Text to classify (example sentence)
text = "I love learning about AI! It's so fascinating."
'''
payload = {
    "inputs": "I love learning about AI! It's so fascinating.",
}
'''

# Make a POST request to the Hugging Face API
response = requests.post(api_url, headers=headers, json={"inputs": text})
#response = requests.post(api_url, headers=headers, json=payload)

if response.status_code == 200:
# Parse and print the results
    classification = response.json()
    print("Predicted label:", classification[0]['label'])
else:
    print(f"Error: {response.status_code}")

