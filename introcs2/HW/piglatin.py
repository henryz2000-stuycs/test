def isVowelUpper(first_letter):
    return (first_letter == "A" \
            or first_letter == "E" \
            or first_letter == "I" \
            or first_letter == "O" \
            or first_letter == "U" \
            or first_letter == "Y")

#print isVowelUpper("A")
#print isVowelUpper("Z")

def isVowelLower(first_letter):
    return (first_letter == "a" \
            or first_letter == "e" \
            or first_letter == "i" \
            or first_letter == "o" \
            or first_letter == "u" \
            or first_letter == "y")

#print isVowelLower("a")
#print isVowelLower("z")

def firstVowel(word):
        return word + "way"

#print firstVowel("of")

def firstVowelPhrase(phrase):
    ans = ""
    while phrase != "":
        if phrase.find(" ") != -1:
            space = phrase.find(" ")
        ans += firstVowel(phrase[:space]) + " "
        phrase = phrase[space + 1:]
    return ans

print "----------------------- FIRST VOWEL PHRASE ---------------------"
print firstVowelPhrase("Asdf asdf")

def isNotVowel(first_letter):
    return (not (isVowelUpper(first_letter) or isVowelLower(first_letter)))

#print isNotVowel("A")
#print isNotVowel("Z")
#print isNotVowel("a")
#print isNotVowel("z")

def makeLower(letter):
    if ord(letter) >= ord("a"):
        return letter
    else:
        return chr(ord(letter) + 32)

#print makeLower("a")
#print makeLower("A")

def makeLowerWord(word):
    ans = ""
    while word != "":
        ans += makeLower(word[0])
        word = word[1:]
    return ans

#print makeLowerWord("TEstIng")

def firstNotVowel(word):
    if isNotVowel(word[0]):
        notVowel = ""
        newWord = word
        while newWord != "" and isNotVowel(newWord[0]):
            notVowel += newWord[0]
            newWord = newWord[1:]
        ans = newWord + makeLowerWord(notVowel) + "ay"
        if ord(word[0]) <= ord("Z"):
            return chr(ord(ans[0]) - 32) + ans[1:]
        else:
            return ans
    else:
        return firstVowel(word)

#print firstNotVowel("Hello")
#print firstNotVowel("hi")

def firstNotVowelPhrase(phrase):
    ans = ""
    while phrase != "":
        space = phrase.find(" ")
        ans += firstNotVowel(phrase[:space]) + " "
        phrase = phrase[space + 1:]
    return ans

#print "----------------------- FIRST NOT VOWEL PHRASE ---------------------"
#print firstNotVowelPhrase("Qwe qwe")

def translate(phrase):
    phrase += " "
    if isVowelUpper(phrase[:phrase.find(" ")]) or isVowelLower(phrase[:phrase.find(" ")]):
        ans = firstVowelPhrase(phrase)
    else:
        ans = firstNotVowelPhrase(phrase)
    return ans[:-1]

#print translate("Nice try guy")
print translate("What are the rules of Pig Latin")
#Assuming no special characters (i.e. only letters)
    
