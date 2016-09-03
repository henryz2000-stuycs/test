# -*- coding: utf-8 -*-
"""
Team Whatever -- Michael Leyderman and Henry Zheng
IntroCS2 pd8
HW44 -- Log: Better Than Bad, It’s Good!
2016-05-10
"""

"""
1. Step 1: Split up story by spaces into list. This will allow us to loop through the list and use the dictionary mode function written previously.
2. Step 2: Use dictionary mode function to create a value of 1 for each instance of a unique word. This will make it efficient.
3. Step 3: Add 1 value for each instance of each word (not including first one). This will increase each value until the end of the story when a mode can be found.
"""

#*******************************
#IGNORE ANYTHING BELOW THIS LINE
#*******************************

def returnFile(file_name):
    story = open(file_name,"r")
    storynew = story.read()
    storynew = storynew.lower()
    story.close()
    storynew = storynew.replace('.',' .')
    storynew = storynew.strip('.')
    return storynew

#test case
print returnFile('story.txt')
