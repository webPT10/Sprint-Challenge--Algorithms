'''
Your function should take in a single parameter (a string `word`)

Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.

Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    counter = 0

    #base case
    if len(word) < 2: # does WORD have less than 2 characters? if so >> 
        return 0    
    
    if word[0:2] == 'th':  # check indices of 0 & 1 of WORD, do they equal 'th'? if so >> 
        counter = 1
    
    return counter + count_th(word[1:])  # call itself 
    # counter increases only if previous if statement is true
    # count_th(word[1:]) >> reruns count_th function checking WORD from indice 1 to end
