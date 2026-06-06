import requests

def get_public_ip():
    try:
        response = requests.get(
            "https://api.ipify.org?format=json",
            timeout=5
        )

        data = response.json()

        return data["ip"]

    except Exception as e:
        return str(e)


ip = get_public_ip()

print(f"Public IP: {ip}")