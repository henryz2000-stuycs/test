# -*- coding: utf-8 -*-
#Team Idklol -- Henry Zheng, Iris Tao
#IntroCS pd8
#HW#36 - 
#2016-05-02

"""
Mechanism for Madlibification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. global vars for lists containing nouns,adjs,verbs.
2. while loops that check if the number of the placeholders of the specified category is >0
3. if so, then replace ONE of them with a randomly selected word from the corresponding lists of words
4. if not, the while loop breaks and move on to the next category of placeholder/gets to the end
5. return the modified story
note: using replace doesnt affect other parts of the story that are not being modified, therefore all the punctuation/indentation can be kept


New Features in Version 2.0:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. allows nouns and verbs to be modified according to differnt tenses PAST/PRESENT and pronouns SINGULAR/PLURAL

"""


#1. madlibify(story) takes a string containing placeholders (<NOUN>, <VERB>,
#and whatever other placeholders
#and returns a string where all placeholders have been replaced with a random string from the appropriate list of strings. 


import random


nouns = ['boy','girl','cat','dog','student','laptop','cookie','ice-cream']
adjs = ['active','fun-sized','considerate','compassionate','competent','delirious','demanding']
verbs = ['adapt','bargain','complain','grunt','joke','question','sigh']
advs = ['abnormally','beautifully','carefully','dangerously','deliberately','genuinely','obediently']


def check(word):
    return (word[-1] == 'a' or \
       word[-1] == 'e' or \
       word[-1] == 'i' or \
       word[-1] == 'o' or \
       word[-1] == 'u')

print check('joke')
print check('not')
        
def madlibify(story):
               
    while story.count('<NOUN')>0:
        entire=story[story.find('<NOUN'):story.index('>',story.find('<NOUN'))+1]  #extract the section btw <NOUN and >
        noun = nouns[random.randrange(len(nouns))]                                #which would be the entire <NOUN-SINGULAR/PLURAL>
        if entire.find('PLURAL') != -1:                                      
            noun += 's'
        story = story.replace(entire, noun ,1)       #added '1' because then it would only replace one of the <NOUN s at a time
        
    while story.count('<VERB')>0:
        entire=story[story.find('<VERB'):story.index('>',story.find('<VERB'))+1]  
        verb = verbs[random.randrange(len(verbs))]
        if entire.find('PAST') != -1:
            if check(verb):
                verb += 'd'
            else:
                verb += 'ed'
        else:
            if entire.find('SINGULAR') != -1:     #add s only if it doesnt have PAST
                verb += 's'
        story = story.replace(entire, verb ,1)

    while story.count('<ADJECTIVE>')>0:          
        adj = adjs[random.randrange(len(adjs))]
        story = story.replace("<ADJECTIVE>", adj ,1)
             
    while story.count('<ADVERB>')>0:
        adv = advs[random.randrange(len(advs))]
        story = story.replace("<ADVERB>", adv ,1)
        
        
    story = story.split(". ")                      #capitalization
    for x in story:                      
        story[story.index(x)] = x.capitalize()
    story = ". ".join(story)
    return story


story1="The <ADJECTIVE> <NOUN-SINGULAR> <VERB-PAST-SINGULAR> <ADVERB> upside down."
print madlibify(story1)
## The compassionate cat grunted genuinely upside down.

story2="The <ADJECTIVE> <NOUN-PLURAL> <VERB-PRESENT-PLURAL> <ADVERB> back and forward."
print madlibify(story2)
## The competent laptops adapt genuinely back and forward.

story3="THE <ADJECTIVE> <NOUN-PLURAL> <VERB-PAST-PLURAL> <ADVERB>, but the <NOUN-SINGULAR>'s <NOUN-SINGULAR> <VERB-PAST-SINGULAR>."
print madlibify(story3)
## The demanding girls grunted deliberately, but the laptop's dog questioned.







