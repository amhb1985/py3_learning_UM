#this is about : Defining a function to make repeated invocations
# import statements for necessary Python modules
#0 like another we must set first the Majule : request
import requests

#2 we define  one Fuction to our word:
def get_rhymes(word):
    #2.1 after that we set a varible as baseURL = "our free source as URL"
    # may be we can search again for some sources for free use
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

    # 4. set up another var to >> using the .json for our responing var
    word_ds = resp.json()    # return the top three words

    # 5. at end we are returning >>
    #5.1 >> [ d['word in 18 lines'] for d in word_ds VAR in 26 line ]
    # if we not set this return we can see whole Dictionary after running the code
    return [d['word'] for d in word_ds]

    #5.2 >> rep.json()
    return resp.json()
 # Return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))
#again test it for another ones:
print(get_rhymes("asha"))




