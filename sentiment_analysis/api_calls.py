import requests

# Set the URL of your FastAPI endpoint
url = "http://localhost:8000/analyze"

sentiment_texts = [
    "Absolutely delighted with my recent purchase! The product exceeded my expectations in every way. It's high-quality, durable, and exactly what I needed. Couldn't be happier!",
    "Extremely disappointed with the service I received. Not only was the delivery delayed multiple times, but the product itself arrived damaged. I expected better, and I won't be shopping here again.",
    "I tried out the new restaurant in town last night. The food was decent, and the service was okay. Nothing outstanding, but nothing terrible either. I might give it another try in the future."
]


for message in sentiment_texts:

    # Define the input data as a dictionary
    data = {"input_string": message}


    # Check if the request was successful (status code 200)
    try:
        
        # Make a POST request to the endpoint
        response = requests.post(url, json=data)
        
        # Print the response from the server
        print(f"The sentiment is {response.json()["result"]["sentiment"]} with a score of {round(response.json()["result"]["score"], 3)}")

    except Exception as err:

        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {err}")