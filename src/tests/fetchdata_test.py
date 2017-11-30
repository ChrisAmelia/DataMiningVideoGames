import unittest
import sys, os, json
sys.path.append("..")

from fetchdata import fetchAppDetails, filterData
from pprint import pprint

class FetchDataMethodsTest(unittest.TestCase):

    def test_fetchAppDetails(self):
        """Returns true if the method fetchAppDetails succeeds, else false.
        This method is tested on the appid 730 (which corresponds to the game CS:GO).
        What is currently tested is only if the method succeeds to fetch existing data,
        not if the data are corrects: it's indicated by the value of the field
        data['appid']['success'].
        """
        appid = '730'
        data = fetchAppDetails(appid)
        success = data[appid]['success']
        self.assertEqual(success, True)

    def test_filterData(self):
        """Returns true if the method filterData succeeds, else false.
        This method is tested on the appid 730 (CS:GO) and on the appid 900 (Zombie Movie).
        Normally, CS:GO has a key 'categories' which Zombie Movie hasn't, in this case
        a default categories [{'description': 'Unknown', 'id': -1}] is automatically affected.
        """
        appid_730 = '730'
        appid_900 = '900'
        try:
            current_path = os.getcwd()
            path_to_filtered_data = current_path + "/../../res/"
            os.chdir(path_to_filtered_data)
            filename = 'filtered_data.json'
            filtered = json.load(open(filename, 'r'))
            success_730 = filtered['730']['categories'][0]['description'] == 'Multi-player'
            success_900 = filtered['900']['categories'][0]['description'] == 'Unknown'
            self.assertEqual(success_730, True)
            self.assertEqual(success_900, True)
        except Exception as e:
            raise e
        finally:
            os.chdir(current_path)

if __name__ == "__main__":
    unittest.main()
