import unittest
import mock
import utils

JSONSTRING = '{\n"images/!!!!beagle snek.jpg": ["dog", "snek"],\n'\
    + '"images/jOWWHiT.jpg": ["raccoon"]\n}\n'
JSONDATA = { "images/!!!!beagle snek.jpg": ["dog", "snek"],
             "images/jOWWHiT.jpg": ["raccoon"] }

# make sure that this contains all values in JSONDATA
KEYWORDS = ["dog", "snek", "raccoon"]



class ScrubmessageTest(unittest.TestCase):
    def scrub_test(self):
        wrd = utils.scrubmessage("Puppers123 and__ cats# a%re very cute!")
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

class LoadjsonfileTest(unittest.TestCase):

    def test_loadjsonfile(_):
        with mock.patch("builtins.open", mock.mock_open(read_data=JSONSTRING)):
            ret = utils.loadjsonfile("fakefile.json")
            assert ret == JSONDATA, "readjsonfile broken"
            

class GetkeywordsTest(unittest.TestCase):

    @mock.patch("utils.loadjsonfile")
    def test_getkeywords(_, mock_loadjsonfile):
        mock_loadjsonfile.return_value = JSONDATA
        keywords = utils.getkeywords()

        res = True

        for word in KEYWORDS:
            if word not in keywords:
                res = False
                
        assert res == True, 'getkeywords broken'


if __name__ == '__main__':
    unittest.main()
            
