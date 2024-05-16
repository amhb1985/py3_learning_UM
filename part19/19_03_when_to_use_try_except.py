
#this is about the when we can use try/exept :
if somekey in d:
    # its there; exrtract the data
    extract_data(d)
else:
    skip_this_one(d)
#.... versus ... 

try:
    extract_data(d)
exept KeyError:
    skip_this_one(d)



