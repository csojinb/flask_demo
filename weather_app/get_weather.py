import requests
from pprint import pprint

def get_weather(location):
    """
    Takes in validated location information and makes an API call to
    the Weather Underground.

    Returns a dict of weather information, or an error message
    """
    wunderground_url_base = (
        'http://api.wunderground.com/api/3bb1446cf63dc3d0/conditions/q/')

    request_url = wunderground_url_base + str(location) + '.json'

    r = requests.get(request_url)
    r = r.json()

    # Look in the console to see the information that comes back from api call!
    pprint(r)

    try:
        weather_description = r['current_observation']['weather']
        weather_description_icon_url = r['current_observation']['icon_url']
        full_location = r[
            'current_observation']['observation_location']['full']

        return {'description': weather_description,
                'icon_url': weather_description_icon_url,
                'full_location': full_location}

    except KeyError:
        error = r['response']['error']['description']

        return {'error': error}