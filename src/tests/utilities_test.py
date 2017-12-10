import unittest, sys
import re
sys.path.append("..")

from utilities import cleanHTML

class UtilitiesMethodsTest(unittest.TestCase):

    def test_cleanHTML(self):
        """Returns true if the tested text doesn't context HTML tags anymore,
        else false.
        """
        raw_html = "This is an <strong>awesome game</strong> made by <i>fans</i>"
        clean = "This is an awesome game made by fans"
        clean_test = cleanHTML(raw_html)
        self.assertEqual(clean_test, clean)

if __name__ == "__main__":
    unittest.main()
