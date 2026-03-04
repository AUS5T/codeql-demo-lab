# Example application code demonstrating a hardcoded API key
# This is intentionally insecure for security scanning demonstrations

import requests

# Hardcoded API key (intentionally exposed)
API_KEY = "sk_live_1234567890_example"

def get_user_data(user_id):
    url = f"https://api.example.com/users/{user_id}"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(url, headers=headers)

    return response.json()


if __name__ == "__main__":
    data = get_user_data("123")
    print(data)
