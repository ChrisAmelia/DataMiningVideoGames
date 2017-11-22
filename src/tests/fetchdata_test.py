import unittest
import sys
sys.path.append("..")

from fetchdata import fetchAppDetails

class FetchDataMethodsTest(unittest.TestCase):

    def test_fetchAppDetails(self):
        """Returns true if the method fetchAppDetails succeeds, else false.
        This method is tested on the appid 730 (which corresponds to the game CS:GO).
        What is currently tested is only if the method succeeds to fetch existing data,
        not if the data are corrects: it's indicated by the value of the field
        data['appid']['success'].
        """
        appid = 730
        data = fetchAppDetails(appid)
        success = data[str(appid)]['success']
        self.assertEqual(success, True)

if __name__ == "__main__":
    unittest.main()
