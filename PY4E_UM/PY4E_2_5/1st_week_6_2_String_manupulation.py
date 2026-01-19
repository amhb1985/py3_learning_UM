# String Concatiention
'''a = "Hallo"
b = a + "nochmal"
print(b)
c = a + " " + b
print(c)
'''

#02_String _comparison#
'''
Wort = 'Apll'

if Wort == "Apfel" :
    print("alles gut, Apfel")
if Wort < 'Apfel' :
   print("Dein Wort, "+ Wort + ' ,kommt bevor dem Apfel.')
elif Wort >'Apfel':
   print("Dein Wort, "+ Wort + ' ,kommt nach dem Apfel.')
else:
    print("alles gut, Apfel")
   
'''
#String Library 

gruesse = "Hallo Bob!"
test02 = "HALLLLLOOOO !!!"
zap = gruesse.lower()
#print(zap)
grosse_test02 = test02.lower()
#wir können direkt .lower in string Format benutzen!
#print("HALLO nochMall!!".lower())
#print(grosse_test02)

#These are the methods: .lower()
'''
Kollege = "Hallo Welt!"
type(Kollege)
dir(Kollege)'''
# so weiter mit the String Library
#das ist eine website für string library:
#https://docs.python.org/3/library/stdtypes.html#string-methods
# das meistens ist anfang mit 
# str + 
#  .casefold()
#  .capitalize()
#  .count()

#String - Part 2 :Searching in a String
'''# we can using the Method .find() for searcing an exact character or Alphabet as String in it 
obst = "Kleine Bananen! "
print("Method for searching of Position:")
print(obst)
pos = obst.find('Ba')
print(pos)
# we can see the Position of the Searching String Ch in it.
'''
#searching and Replace:
'''gruesse = "Hallo Andy!"
nstr = gruesse.replace("Andy","Daniel")
nstr = gruesse.replace("H","X")
print(gruesse)
print(nstr)'''

#Stripping Whitespace. >>>  .lstrip() , .rstrip(), .strip() 
'''gruesse = "    Hallo Andy!   "
lstrip = gruesse.lstrip()
print(gruesse)
print(lstrip)
rstrip = gruesse.rstrip()
print(rstrip)
strip = gruesse.strip()
print(strip)
'''

'''#Prefix
#Start String with Prefex
line = "Mit Freundlischen Gruesse"
Start = line.startswith("mit")
print(Start)
'''
#parsing and Extracting
data = "From amhb.aaa@uct.ac.za Sat Apr 08 11:22:16 2025"
atops = data.find('@')
print(atops)

sppos = data.find(' ',atops)
print(sppos)

host = data[atops+1 : sppos]
print(host)
#find and show position
# this find between 2 String here @ and another as Space an show the result

