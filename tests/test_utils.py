import unittest
import mock
import utils

utils.KEYWORDS_FILE = "test_keywords.json"

class ScrubmessageTest(unittest.TestCase):
    def scrub_test(self):
        wrd = utils.scrubmessage("Puppers and cats are very cute!")
        assert wrd == ["puppers", "and", "cats", "are", "very", "cute"]\
            , 'should be ["puppers", "and", "cats", "are",'\
            + '"very", "cute"]'

class KeywordsinmessageTest(unittest.TestCase):

    @mock.patch("utils.getkeywords")
    def test_keywordsinmessage(self, mock_getkeywords):

        mock_getkeywords.return_value = ["dog", "cat", "lizard"]
        msg = "@wasdmurai Can I have a dog?"
        msg = utils.keywordsinmessage(msg)
        
        assert msg == ["dog"], 'keywordsinmessage broken'



case1 = ScrubmessageTest()
case2 = KeywordsinmessageTest()

case1.scrub_test()
case2.test_keywordsinmessage()

"""
images = utils.loadjsonfile(utils.KEYWORDS_FILE)
chosen = "raccoon"

filtered = [k for k,v in images.items() if chosen in v]

assert filtered == ["images/jOWWHiT.jpg"]\
    , 'loadjsonfile broken'

allwords = utils.getkeywords()
res = True

for elem in ["dog", "snek", "raccoon"]:
    if elem not in allwords:
        res = False
        
assert res == True, 'getkeywords broken'

"""


print("All tests passed")
