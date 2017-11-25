import urllib.request, json
from pprint import pprint

def fetchAppDetails(appid, write=False):
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
        success = data[str(appid)]['success']
        if write:
            if success:
                f = open(str(appid) + '.json', 'w')
                json.dump(data, f)
            else:
                print('AppID \'' + str(appid) + '\' doesn\'t exist.')
        return data

# To fetch data from Steam API (which authorizes around 200 requests within a short period of seconds).
# A Steam game's appID is always a multiple of 10 except if it's a beta-game.
# if __name__ == "__main__":
    # for appid in range(4510, 5001):
        # if (appid % 10 == 0):
            # fetchAppDetails(appid, True)
        # else:
            # pass
