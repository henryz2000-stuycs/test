#Henry Zheng
#IntroCS2 pd8
#HW21 -- Cereal Grade Encryption
#2016-03-28

#1.

def rot13Chr(ch):
    newnum = ord(ch)                                           #sets newnum to be the ASCII code of the character
    if newnum >= ord("A") and newnum <= ord("Z"):              #if the character is an uppercase letter
        newnum -= 65                                           #subtracts the ASCII code of "A" to get to traditional 1-26 letter format
        newnum += 13                                           #sets up rot13 encoding
        newnum %= 26                                           #          "  
        newnum += 65                                           #changes back to ASCII code
    else:                                                      #if the character is a lowercase letter
        newnum -= 97                                           #subtracts the ASCII code of "a" to get to traditional 1-26 letter format
        newnum += 13                                           #sets up rot13 encoding
        newnum %= 26                                           #          "
        newnum += 97                                           #changes back to ASCII code
    return chr(newnum)

print rot13Chr("a")                                            #should be "n"
print rot13Chr("m")                                            #should be "z"
print rot13Chr("z")                                            #should be "m"
print rot13Chr("A")                                            #should be "N"
print rot13Chr("M")                                            #should be "Z"
print rot13Chr("Z")                                            #should be "M"

#2.

def printEmAll():
    num = ord("A")                                             #starts off number as the ASCII code for the first letter of the alphabet
    ans = ""                                                   #sets answer to be an empty string
    while num <= 122:                                          #in order to stop when the end of the alphabet is reached ("z")
        ans += chr(num) + " <-> " + rot13Chr(chr(num)) + "\n"  #adds to the answer the letter of the number and the rot13 equivalent of the number
        num += 1                                               #goes onto the next letter
        if num == 90:                                          #in order to avoid special characters
            num = 97                                           #jumps to lowercase letters
    print ans

printEmAll()
#should be
#A <-> N
#B <-> O
#...
#a <-> n
#b <-> o
#...and so on

#3.

def rot13Wrd(word):
    ans = ""                                                   #sets answer to be an empty string
    index = 0                                                  #starts off at the beginning of the word string
    while index < len(word):                                   #in order to avoid repeating the answer over and over (infinite loop)
        ans += rot13Chr(word[index])                           #adds to the answer the rot13 equivalent of that character
        word = word[1:]                                        #goes onto the next character of the word string
    return ans                                                 #returns the answer

print rot13Wrd("JABBERWOCKY")                                  #should be "WNOOREJBPXL"
    
