import requests
# Set up the Hugging Face API URL for text-to-image generation (DALL-E model)
api_url = "https://api-inference.huggingface.co/models/dalle-mega"

# Replace with your Hugging Face API key
token = {
    "Authorization": "Bearer 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"
}

# Example text prompt
text_prompt = "A futuristic city with flying cars during sunset."

# Send the POST request to Hugging Face's API
response = requests.post(api_url, headers=token, json={"inputs": text_prompt})

# Check if the request was successful
if response.status_code == 200:
    image_data = response.json()
    image_url = image_data['image_url'] # URL to the generated image
    print(f"Image generated! View it at: {image_url}")
else:
    print("Error: Unable to generate image.")
