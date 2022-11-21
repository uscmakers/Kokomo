import requests

key = "2ee39e4a62c53b8925eedda4e64b3e0f3eed31d1d15cad2cc810a34d073c37f6"

response = requests.get("https://serpapi.com/search", params={"engine": "google", "q": "aruba jamaica", "api_key": key})

response_json = response.json()

knowledge_graph = response_json["knowledge_graph"]
song_name = knowledge_graph["title"]
artist_name = knowledge_graph["artist"]

print(song_name)
print(artist_name)
