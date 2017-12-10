import json, os

from pprint import pprint
from utilities import cleanHTML

def vectorizeData():
    """Returns a list containing the description of each game present in 'filtered_data.json'.
    Returns:
        a list; description + publishers
    """
    lst = []
    curdir = os.curdir
    try:
        new_path = curdir + "/../res/"
        os.chdir(new_path)
        filename = 'filtered_data.json'
        data = json.load(open(filename))
        for key in data:
            description = data[key]['detailed_description']
            publishers = ''.join(data[key]['publishers'])
            # Remove HTML tags, tabs, newlines
            description = cleanHTML(description)
            description = description.replace("\t", "")
            description = description.replace("\n", "")
            description = description.replace("\r", "")
            # 'Publishers' is believed to be an important key, this is why it's added twice
            result = description + " " + publishers + " " + publishers
            lst.append(result)
    except Exception as e:
        raise e
    finally:
        os.chdir(curdir)
    return lst
