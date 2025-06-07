import requests
import urllib.parse

def get_movie_details(title, api_key):
    title = title.strip()
    encoded_title = urllib.parse.quote(title)

    # Primary search using exact title
    url = f"http://www.omdbapi.com/?t={encoded_title}&plot=full&apikey={api_key}"
    res = requests.get(url).json()

    if res.get("Response") == "True":
        plot = res.get("Plot", "N/A")
        poster = res.get("Poster", "N/A")
        return plot, poster

    # Fallback: search and get first result's imdbID
    search_url = f"http://www.omdbapi.com/?s={encoded_title}&apikey={api_key}"
    search_res = requests.get(search_url).json()

    if search_res.get("Response") == "True" and "Search" in search_res:
        first_result = search_res["Search"][0]
        imdb_id = first_result.get("imdbID")

        if imdb_id:
            details_url = f"http://www.omdbapi.com/?i={imdb_id}&plot=full&apikey={api_key}"
            details_res = requests.get(details_url).json()
            if details_res.get("Response") == "True":
                plot = details_res.get("Plot", "N/A")
                poster = details_res.get("Poster", "N/A")
                return plot, poster

    return "N/A", "N/A"
