

#this is about : Defining a function to make repeated invocations
# import statements for necessary Python modules
#0 like another we must set first the Majule : request
import requests

#2 we define  one Fuction to our word:
def get_rhymes(word):
    #2.1 after that we set a varible as baseURL = "our free source as URL"
    baseurl = "https://api.datamuse.com/words"
    #2.2 set up an empty {Dictionary}
    params_diction = {} # Set up an empty dictionary for query parameters

    #2.3 set up two functions for our query paramthers: 
    #   >>  1 ["rel_rhy"] = word   
    #   >>  2  ["max"] = "3"
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results

    # 3. set uo now one RESPOND var to  get requst 
            #request.get(URL_var, param s= paramethers_var )
    resp = requests.get(baseurl, params=params_diction)

    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    return resp.json() # Return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))
print(get_rhymes("dash"))


