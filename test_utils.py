import utils

utils.KEYWORDS_FILE = "test_keywords.json"

wrd = utils.scrubmessage("Puppers and cats are very cute!")
assert wrd == ["puppers", "and", "cats", "are", "very", "cute"]\
    , 'should be ["puppers", "and", "cats", "are",'\
    + '"very", "cute"]'

msg = "@wasdmurai Can I have a dog?"
msg = utils.keywordsinmessage(msg)
assert msg == ["dog"], 'keywordsinmessage broken'

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

