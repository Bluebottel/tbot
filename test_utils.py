import utils

keywords = utils.getkeywords()
allwords = []

#for keys, value in keywords.items():
#    for tag in value:
#        if tag not in allwords:
#            allwords.append(tag)

#print(keywords)


#wrd = utils.scrubmessage("Puppers and cats are very cute!")
#print(wrd)

msg = "@wasdmurai Can I have a corgi?"
print(utils.keywordsinmessage(msg))




print(utils.scrubmessage(msg))


# TODO: make these into real tests
"""
images = utils.loadjsonfile(utils.KEYWORDS_FILE)
chosen = "gecko"

filtered = [k for k,v in images.items() if chosen in v]
print(filtered)
"""
