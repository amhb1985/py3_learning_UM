

#Write a program that finds the most used 7 letter word in scarlet3.txt.

'''
d = { 'work': 'success', 'success': 'failure', 'failure': 'money', 'time': 'work', 'industry': 'time'}


print(d['industry'])
'''

#testing and reading

#1.one Dictionary list:
d =  {'a': 2, 'b': 3, 'c': 1}

#2. creating an empty Dic as name"e" :
e = {}

#3. making Iritate or Loop with for in:
#for the resault of full the empty Dict:
#it will invers the all of keys < >  value
for c in d:
    e[d[c]] = c
print (e)