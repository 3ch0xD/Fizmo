import requests

url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMzhhYjY2MDkyODIyZDNiMTUwYzA1MWZiODQ2ZjcwYyIsIm5iZiI6MTcyMTY1MzAzOC44MTc0NDcsInN1YiI6IjY2OGViY2QxYjQyN2EwNzUyNzVhY2RmZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.npVnlPRmCUWluhXgHDvgBbsdmIVkeWZE48MjbFTRoSU"
}

response = requests.get(url, headers=headers)
data_showcase_movie = response.json()

showcase_movie = data_showcase_movie['results'][0]

vote_average = data_showcase_movie['results'][0]['vote_average']
rounded_vote_average = round(vote_average, 1)

overview = showcase_movie['overview']
if len(overview) > 100:
    overview = overview[:100] + '...' 

