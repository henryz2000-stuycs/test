#Team The One Near Genkina's Desk' -- Michael Leyderman, Manjit Singh, Henry Zheng
#IntroCS2 pd8
#HW22 -- Further Exploration in Toy Encryption
#2016-03-29

"""
For rotNChr, we created an ifelse statement to check whether it was a capital
or a lowercase letter, then change it to the traditional 1-26 letter format, then
modding it by 26 in order to change the numbers above 26 to start back at "a".
Finally, we change it back to ASCII code by adding what we subtracted in the beginning.
"""

"""
For rotN, we created an empty string and used rotNChr to replace every
letter of the word given and add it to the empty string to formulate the answer.
"""

def rot13Chr_new(ch):
    #the below code works works for when the string ch is a capital letter
    if ch.upper()==ch:
        offset = ord('A') #65
    else:
        offset = ord('a') #97
    #the code above applies when the string is a lowercase letter
    return chr( (ord(ch) + 13 - offset) % 26 + offset )


def rotNChr(ch,n):
    newnum = ord(ch)                                           #sets newnum to be the ASCII code of the character
    if newnum >= ord("A") and newnum <= ord("Z"):              #if the character is an uppercase letter
        newnum -= 65                                           #subtracts the ASCII code of "A" to get to traditional 1-26 letter format
        newnum += n                                            #sets up rot13 encoding
        newnum %= 26                                           #          "  
        newnum += 65                                           #changes back to ASCII code
    elif newnum >= ord("a") and newnum <= ord("z"):                                                      #if the character is a lowercase letter
        newnum -= 97                                           #subtracts the ASCII code of "a" to get to traditional 1-26 letter format
        newnum += n                                            #sets up rot13 encoding
        newnum %= 26                                           #          "
        newnum += 97                                           #changes back to ASCII code
    else:
	return ch
    return chr(newnum)

print rotNChr("a", 13)                                            #should be "n"
print rotNChr("m", 13)                                            #should be "z"
print rotNChr("z", 13)                                            #should be "m"
print rotNChr("A", 13)                                            #should be "N"
print rotNChr("M", 13)                                            #should be "Z"
print rotNChr("Z", 13)                                            #should be "M"


#rot13(phrase) with an extra parameter, n, if we were to replace rot13 with rotN.
#To use regular rot13, just insert 13 in place of n when calling the function.

def rotN(word, n):
    ans = ""                                                   #sets answer to be an empty string
    index = 0                                                  #starts off at the beginning of the word string
    while index < len(word):                                   #in order to avoid repeating the answer over and over (infinite loop)
        ans += rotNChr(word[index], n)                           #adds to the answer the rot13 equivalent of that character
        word = word[1:]                                        #goes onto the next character of the word string
    return ans                                                 #returns the answer

print rotN("JABBERWOCKY", 13)                                  #should be "WNOOREJBPXL"
print rotN("Justin Bieber", 13)                                #should be "Whfgva Ovrore"
print rotN("Justin Bieber? Like, OMG!!! He's my hero!", 13)    #should be "Whfgva Ovrore? Yvxr, BZT!!! Ur'f zl ureb!"


def test(word):
    n=1                                                        #if in rotN, n starts at 1
    ans=""                                                     #starts off the answer as a blank string
    while n<26:                                                #returns all of the possible string of characeters when n = 1, 2, ... 25
        ans += str(n) + ". " + rotN(word,n) + "\n"         #returns in format
        n += 1                                                 #adds one to n to setup the next string sequence
    print ans                                                  #prints the answer

test("deoh")   #23
test("ufwyd")  #21
test("udm")    #11
test("Cppkg ctg aqw QM?")  #24
test("Abzqdqvo nwz xmznmkbqwv mdmz aqvkm Q eia i avwbvwam")  #18
test("Apnly nva av obua, ipyk nva av msf; Thu nva av zpa huk dvukly, 'Dof, dof, dof?' Apnly nva av zsllw, ipyk nva av shuk; Thu nva av alss optzlsm ol buklyzahuk.")  #19
test("Roi roi! Ry ry! Cyzr-Pbycr CSXQ! tecd cdyvo dro cryg!")  #16

"""
We just changed up our old homework function to take into consideration if n was not 13.
Our original rotNChr function changed by adding n to the newnum instead of adding 13.
"""
    
