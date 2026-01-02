#so, today we are going again testing with The Slice Operator:

julia = ("Julia","Roberr", 1967,"Duplicity",1988,1976, "Georg" )
infos = [1, 22 , "Golf"]

'''
print(julia[2])
print(julia[2:4])

#asking abou type of list or tuple
print(type(julia))
print(type(infos))
'''

#print(len(julia))
#print(len(infos))

#add another paragraf or exactly Index to the tuple
julia = julia[:3] + ("eat ,Pray, love", 2010) + julia[:5]
#print(julia)

# NOTE: in the list but it will not working!!
#infos = [:1] + ["let do it for "] + [:3]
#print(infos)

#next we try to make one SubGroup from one main
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst[8:10]
print (sub_lst)
