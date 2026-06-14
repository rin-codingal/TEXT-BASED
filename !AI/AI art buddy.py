import requests
from PIL import Image
from io import BytesIO

api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImVkMDJjMGJjMjUwZGQ1NDEwNGRlYTUwZGUzMDVkM2UxIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDQtMjZUMTE6MDE6NDkuODk2MjE0In0.Nt2t7Rh1X6xzYhlSAxTyp_3MIi9KXmu-KqGAX39t-j0"

user_input = input("Enter image description: ")
url = "https://api.monsterapi.ai/v1/generate/txt2img"
header = {"Authorization": f"Bearer {api_token}"}
response = requests.post(url, json={"prompt": user_input, "safe_filter": True}, headers=header)

if response.status_code == 200 :
    print("Loading.. the image may take few seconds")
    process_id = response.json().get("process_id")

    while True:
        status_data = requests.get(f"https://api.monsterapi.ai/v1/status/{process_id}", headers=header).json()
        status = status_data.get("status")

        if status == "COMPLETED":
            image_url = status_data['result']['output'][0]
            img = Image.open(BytesIO(requests.get(image_url).content)).show()
            break
        elif status == "FAILED":
            print("image generation failed")
            break

else:
    print(f"Error: {response.status_code}")