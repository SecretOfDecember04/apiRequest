import requests

# URL of the new API
url = "http://api.nbp.pl/api/cenyzlota/last/30/?format=json"

try:
    # Sending a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Display the response JSON in a formatted way
        data = response.json()

        # Print the results
        print("Gold prices for the last 30 days:\n")
        for record in data:
            print(f"Date: {record['data']}, Price: {record['cena']} PLN")
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
