import time
import requests
import os

def get_coordinates(address: str):
    url = os.getenv('API_GEOCODE')
    payload = {"address": address}

    connection_status = False
    retry_limit = 10
    retry = 0
    while not connection_status and retry <= retry_limit:
        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}")
                connection_status = True
            else:
                print(f"Error: {response.status_code} - {response.json().get('detail')}")
                connection_status = True
        except requests.exceptions.ConnectionError:
            print("Server not ready, retrying...")
            retry += 1
            time.sleep(2)
    
    if not connection_status:
        print("Failed to connect to the server after multiple attempts.")

if __name__ == "__main__":
    while True:
        #1600 Pennsylvania Ave NW, Washington, DC 20500
        user_input = input("Enter an address (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        get_coordinates(user_input)