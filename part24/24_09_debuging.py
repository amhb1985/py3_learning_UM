
#this is about debugging

import requests

#we set one varible to get requests from one URl as our source
r = requests.get("https://api.datamuse.com/words", params ={"rel_rhy": "funny"})
print(r.text)
print(r.url)


