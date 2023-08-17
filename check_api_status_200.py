import requests

def check_api(url):
    try:
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            # API is working
            print("API is working")
        else:
            # API request failed
            print("API request failed. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        # Error occurred during API request
        print("Error occurred during API request:", str(e))

# Example usage
api_url = "https://test.api.amadeus.com/v1/shopping/availability/flight-availabilities" # Replace with the API endpoint URL

check_api(api_url)
