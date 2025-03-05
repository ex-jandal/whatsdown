import requests

def get_public_ip():
    try:
        # Query the external service to get your public IP address
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()  # Check for HTTP errors
        return response.text.strip()  # Get the IP address from the response
    except requests.RequestException as e:
        print("Error retrieving public IP:", e)
        return None

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print("My public IP is:", public_ip)
    else:
        print("Could not retrieve public IP.")

