import urllib.request, json
from pprint import pprint

def fetchAppDetails(appid):
    """Returns the fetched data from Steam API.
    Steam API's format is: https://api.steampowered.com/<interface>/<method>/v<version>/
    In this case, it should be: http://store.steampowered.com/api/appdetails/?appids=VALUE&format=json

    Args:
        appid (int): Every Steam game has an unique ID called AppID.

    Returns:
        data; a dictionnary containing the fetched data in JSON format.
        If the data have been correctly fetched then the field data['appid']['success']
        should be set to True, else False.
    """
    host = "http://store.steampowered.com"
    interface = "api"
    method = "appdetails"
    get = "?appids="
    format = "format="
    file_type = "json"
    request = host + "/" + interface + "/" + method + "/" + get + str(appid) + "&" + format + file_type
    with urllib.request.urlopen(request) as url:
        data = json.loads(url.read().decode())
        return data
