# -*- coding: utf-8 -*-
#Team Idklol -- Henry Zheng, Iris Tao
#IntroCS pd8
#HW#36 - Put Your Plan Into Action
#2016-04-21

'''
Mechanism for Madlibification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. global vars for lists containing nouns,adjs,verbs.
2. while loops that check if the number of the placeholders of the specified category is >0
3. if so, then replace ONE of them with a randomly selected word from the corresponding lists of words
4. if not, the while loop breaks and move on to the next category of placeholder/gets to the end
5. return the modified story
note: using replace doesnt affect other parts of the story that are not being modified, therefore all the punctuation/indentation can be kept
'''



#1. fillBlanks(story) takes a string containing placeholders of the form <NOUN>, <VERB>, etc. and returns a string where all placeholders have been replaced with a random string from the appropriate list of strings. (E.g., An occurrence of <NOUN> would be replaced with an element of [“dog”, “cat”, “truck”], selected at random.) Uses global variables nouns, verbs, adjs, advs.


import random

nouns = ['boy','girl','cat','dog','student','mouse','ice-cream']
adjs = ['active','fun-sized','considerate','compassionate','competent','delirious','demanding']
verbs = ['adapts','bargains','complains','grunts','jokes','questions','sighs']
advs = ['abnormally','beautifully','carefully','dangerously','deliberately','genuinely','obediently']
        
def fillBlanks(story):
    while story.count('<NOUN>')>0:  
        noun = nouns[random.randrange(len(nouns))] #replace the placeholder with a randomly selected word from the lists of nouns/adjs/verbs/etc...
        story = story.replace("<NOUN>", noun ,1)
    while story.count('<ADJECTIVE>')>0:            #you can use count because the story is a string (not list)
        adj = adjs[random.randrange(len(adjs))]
        story = story.replace("<ADJECTIVE>", adj ,1)
    while story.count('<VERB>')>0:
        verb = verbs[random.randrange(len(verbs))]
        story = story.replace("<VERB>", verb ,1)
    while story.count('<ADVERB>')>0:
        adv = advs[random.randrange(len(advs))]
        story = story.replace("<ADVERB>", adv ,1)
    story = story.split(". ")
    for x in story:
        story[story.index(x)] = x.capitalize()
    story = ". ".join(story)
    return story

#story= "The <ADJECTIVE> <NOUN> <VERB> <ADVERB> upside down."
#print fillBlanks(story)

#story2="If <NOUN> likes <NOUN>, then you will see how <ADJECTIVE> punctuation is. And if you have more than one sentence, \
#this function still works <ADVERB> and <ADVERB>. This is how <ADJECTIVE> we are."
#print fillBlanks(story2)

story3="test story. <ADVERB> the <ADJECTIVE> <NOUN> <VERB> down on the <NOUN>"
print fillBlanks(story3)
