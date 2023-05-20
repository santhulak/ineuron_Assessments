import requests
import json

# API endpoint URL
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response content to JSON format
    data = json.loads(response.content)

    # Extract the required data attributes from the JSON response
    show_id = data["id"]
    show_url = data["url"]
    show_name = data["name"]
    
    episodes = data["_embedded"]["episodes"]
    
    # Iterate over each episode and extract the desired attributes
    for episode in episodes:
        episode_id = episode["id"]
        episode_url = episode["url"]
        season_number = episode["season"]
        episode_number = episode["number"]
        episode_type = episode["type"]
        air_date = episode["airdate"]
        air_time = episode["airtime"]
        runtime = episode["runtime"]
        average_rating = episode["rating"]["average"]
        summary = episode["summary"].replace("<p>", "").replace("</p>", "")
        medium_image_link = episode["image"]["medium"]
        original_image_link = episode["image"]["original"]
        
        # Print the extracted data attributes for each episode
        print("Episode ID:", episode_id)
        print("Episode URL:", episode_url)
        print("Season Number:", season_number)
        print("Episode Number:", episode_number)
        print("Episode Type:", episode_type)
        print("Air Date:", air_date)
        print("Air Time:", air_time)
        print("Runtime:", runtime)
        print("Average Rating:", average_rating)
        print("Summary:", summary)
        print("Medium Image Link:", medium_image_link)
        print("Original Image Link:", original_image_link)
        print("-------------------------")

else:
    print("Failed to retrieve data from the API.")

