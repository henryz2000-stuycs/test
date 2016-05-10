"""
Team Public Relations -- Gilvir Gill and Henry Zheng, Director of Public Relations
IntroCS2 pd8
HW43 -- Plan for Word Frequency Tallying
2016-05-09
"""
def printFile(file_name):
    story = open(file_name,"r")
    print story.read()

#test case
printFile('story.txt')



"""
Core Algorithm for Word Frequence Tallying
------------------------------------------------
1.  Save the file in the form of a plaintext to  a local variable that can be manipulated.
2.  Split the novel into lists of the words with no delimiters (this is destructive to the text but it doesn't matter).
3.  Use the dictionary mode function we did for HW yesterday to return the most occuring word.

Things to deal with and possible solutions
------------------------------------------------
1. The same word with different capitalization: While creating the list, make all words lowercase.
2. Multiple words with same occurence: return lists by modifying dictionary mode function.
3. Slow Function: Try to simplify everything into as few iterations as possible by combining steps (this is going to be thousands of words, so very important!)
"""
