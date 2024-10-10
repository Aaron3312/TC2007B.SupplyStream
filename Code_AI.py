import requests
import base64


API_URL = "https://api-inference.huggingface.co/models/openai/clip-vit-base-patch32"
headers = {"Authorization": "Bearer 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"}

def query(data):
	with open(data["image_path"], "rb") as f:
		img = f.read()
	payload={
		"parameters": data["parameters"],
		"inputs": base64.b64encode(img).decode("utf-8")
	}
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
    "image_path": "kitty.jpg",
    "parameters": {"candidate_labels": ["cat", "dog", "llama", "bottle", "car", "banana", "computadora"]},
})

print(output)