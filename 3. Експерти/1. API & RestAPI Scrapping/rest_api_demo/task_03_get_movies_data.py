# http://www.omdbapi.com/?apikey=cfdf5a02&t=Terminator&y=1984

import json
import requests
from Lecture_14_services.api_config import omdbapi_key

URL = 'http://www.omdbapi.com'
API_KEY = omdbapi_key


def get_response(key, value):
    return requests.get(URL, params={key: value,
                                    'apikey': API_KEY})


def get_movie_details_by_title(title):
    response = get_response("t", title)
    json_text = json.loads(response.text)

    search_list = ['Actors', "Title", "Director"]

    return [(search_word, json_text.get(search_word)) for search_word in search_list]

    # details = []
    # for search_word in search_list:
    #     details.append((search_word, json_text.get(search_word)))
    #
    # return details


def search__by_title(title):
    response = get_response("s", title)
    json_text = json.loads(response.text)
    movies = json_text.get('Search')

    return [movie.get("Title") for movie in movies]

    # titles = []
    # for movie in movies:
    #     titles.append(movie.get('Title'))
    #
    # return titles


details = get_movie_details_by_title("Batman")
print(details)

titles = search__by_title("Terminator")
print(titles)
