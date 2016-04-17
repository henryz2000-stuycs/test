#Team Eamtay -- Kaia Tien, Henry Zheng, Ginevra Lee
#IntroCS2 pd 8
#HW23-- Anslatingtray Englishway intoway Igpay Atinlay
#2016-03-30


"""
Pig Latin Rules:
1. If the word begins with a vowel, just add -way
2. Otherwise, remove all the consonants at the beginning of the word until
you reach a vowel, put them at the end of the word and add -ay.

Outline:
Write a function for each step. Create one big function using each of the
other functions for testing the type of word. 

Development Plan:
1. The simplest function that we can test first is testing for a vowel at
the beginning, and then adding -ay based on if it is true or falsel. 
2. We can add to that by adding a while loop to find the first vowel occurence
and then removing everything in front of that and putting it at the end and adding -ay.

Development Log:
2016-03-29  2:00
All the members of the team came up with the rules and plan.: Task accomplished!

"""

def isChar(ch):
    return (ord("A") <= ord(ch) <= ord("Z")) or (ord("a") <= ord(ch) <= ord("z"))  #returns if it is a letter or not

def isVowelUpper(first_letter):       #returns if the letter is an uppercase vowel
    return (first_letter == "A" \
            or first_letter == "E" \
            or first_letter == "I" \
            or first_letter == "O" \
            or first_letter == "U" \
            or first_letter == "Y")

#print isVowelUpper("A")  should be True
#print isVowelUpper("Z")  should be False

def isVowelLower(first_letter):        #returns if the letter is a lowercase vowel
    return (first_letter == "a" \
            or first_letter == "e" \
            or first_letter == "i" \
            or first_letter == "o" \
            or first_letter == "u" \
            or first_letter == "y")

#print isVowelLower("a")  should be True
#print isVowelLower("z")  should be False

def firstVowel(word):                      #if the first letter of the word is a vowel
    if isChar(word[-1]):
        return word + "way"
    else:
        word = word[:-1]
        return word + "way" + word[-1]

#print firstVowel("of")  should be "ofway"

def firstVowelPhrase(phrase):                      #same thing as firstVowel(word), except can be used for sentences
    ans = ""
    while phrase != "":
        if phrase.find(" ") != -1:
            space = phrase.find(" ")
        ans += firstVowel(phrase[:space]) + " "
        phrase = phrase[space + 1:]
    return ans

print "----------------------- FIRST VOWEL PHRASE ---------------------"
print firstVowelPhrase("Asdf asdf")  #should be "Asdfway asdfway"

def isNotVowel(first_letter):                                                  #returns if first letter is not a vowel
    return (not (isVowelUpper(first_letter) or isVowelLower(first_letter)))

#print isNotVowel("A")  should be False
#print isNotVowel("Z")  should be True
#print isNotVowel("a")  should be False
#print isNotVowel("z")  should be True

def makeLower(letter):                #makes the letter lowercase
    if ord(letter) >= ord("a"):
        return letter
    else:
        return chr(ord(letter) + 32)

#print makeLower("a")  should be "a"
#print makeLower("A")  should be "a"

def makeLowerWord(word):               #makes the first letter of the word lowercase
    ans = ""
    while word != "":
        ans += makeLower(word[0])
        word = word[1:]
    return ans

#print makeLowerWord("TEstIng")  should be "testing"

def firstNotVowel(word):                                             #if the first letter of the word is not a vowel
    if isNotVowel(word[0]):
        notVowel = ""
        punc = 0
        if isChar(word[-1]):
            newWord = word
        else:
            newWord = word[:-1]
            punc += 1
        while newWord != "" and isNotVowel(newWord[0]):
            notVowel += newWord[0]
            newWord = newWord[1:]
        ans = newWord + makeLowerWord(notVowel) + "ay"
        if ord(word[0]) <= ord("Z"):
            if punc == 0:
                return chr(ord(ans[0]) - 32) + ans[1:]
            else:
                return chr(ord(ans[0]) - 32) + ans[1:] + word[-1]
        else:
            if punc == 0:
                return ans
            else:
                return ans + word[-1]
    else:
        return firstVowel(word)

#print firstNotVowel("Hello")  should be "Ellohay"
#print firstNotVowel("hi")     should be "ihay"

def firstNotVowelPhrase(phrase):                    #same thing as firstNotVowel, but can be used on sentences
    ans = ""
    while phrase != "":
        space = phrase.find(" ")
        ans += firstNotVowel(phrase[:space]) + " "
        phrase = phrase[space + 1:]
    return ans

#print "----------------------- FIRST NOT VOWEL PHRASE ---------------------"
#print firstNotVowelPhrase("Qwe qwe")  should be "Eqway eqway"

def translate(phrase):                                                                      #overall wrapper function incorporating all previous functions
    phrase += " "
    if isVowelUpper(phrase[:phrase.find(" ")]) or isVowelLower(phrase[:phrase.find(" ")]):
        ans = firstVowelPhrase(phrase)
    else:
        ans = firstNotVowelPhrase(phrase)
    return ans[:-1]

#print translate("Nice try guy")                     #should be "Icenay ytray uygay"
print translate("What are the rules of Pig Latin")   #should be "Atwhay areway ethay ulesray ofway Igpay Atinlay"
#Assuming no special characters (i.e. only letters)  
print translate("What are the rules of Pig Latin?")  #should be "Atwhay areway ethay ulesray ofway Igpay Atinlay?"
print translate("Hi, my name is Bob.")               #should be "Ihay, ymay amenay isway Obbay."
