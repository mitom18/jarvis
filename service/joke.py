import requests


def get_programming_joke():
    joke = "// This line doesn't actually do anything, but the code stops working when I delete it."
    response = requests.get(
        "https://sv443.net/jokeapi/v2/joke/Programming?format=txt&type=single")
    if (response.status_code == 200):
        joke = response.text
    return joke
