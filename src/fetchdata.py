import urllib.request, json, os
from pprint import pprint

def fetchAppDetails(appid, write=False):
    """Returns the fetched data from Steam API.
    Steam API's format is: https://api.steampowered.com/<interface>/<method>/v<version>/
    In this case, it should be: http://store.steampowered.com/api/appdetails/?appids=VALUE&format=json

    Args:
        appid (int): Every Steam game has an unique ID called AppID.
        write (boolean): Set it to True to write the fetched data into a json file

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

def _filterData(data):
    """See method filterData().

    Args:
        data (dict);  return value of the method fetchAppDetails()

    Returns:
        filtered data
    """
    filtered = {}
    appid = ''
    for key in data:
        appid = key
        break
    shorcut = data[appid]['data']
    filtered['appid'] = appid
    filtered['name'] = shorcut['name']
    filtered['is_free'] = shorcut['is_free']
    filtered['detailed_description'] = shorcut['detailed_description']
    filtered['publishers'] = shorcut['publishers']
    # filtered['about_the_game'] = shorcut['about_the_game']
    # filtered['short_description'] = shorcut['short_description']
    return filtered

def filterData():
    """Returns a dictionnary containing filtered data from given data.
    The filter is applied on labels that are considered 'important' such as
    the name, details of the game, categories, etc.
    See res/label.txt, labels that are considered as important are precede
    by '>' (relevant) or '>>' (very relevant).

    Returns:
        filtered data
    """
    gameList = {}
    try:
        current_path = os.getcwd()
        os.chdir(current_path + "/../res/data/")
        for filename in os.listdir(os.getcwd()):
            data = json.load(open(filename))
            filtered = _filterData(data)
            appid = filtered['appid']
            gameList[appid] = filtered
    except Exception as e:
        raise e
    finally:
        os.chdir(current_path)
    return gameList

# Fetch data from Steam API (which authorizes around 200 requests within a short period of seconds).
# A Steam game's appID is always a multiple of 10 except if it's a beta-game.
# if __name__ == "__main__":
    # for appid in range(4510, 5001):
        # if (appid % 10 == 0):
            # fetchAppDetails(appid, True)
        # else:
            # pass

# if __name__ == "__main__":
    # d = filterData()
    # with open('filtered_data.json', 'w') as fp:
        # json.dump(d, fp)
