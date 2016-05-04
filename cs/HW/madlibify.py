#!/usr/bin/python
print "Content-type:text/html\n"
print ""


#Team Idklol -- Henry Zheng, Iris Tao
#IntroCS pd8
#HW#38 -- Tune Your Engine
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

"""
1. How did your team deal with punctuation?
We didn't really deal with punctuation itself because our code only replaces the placeholders in the sentences.
2. How did at least 2 other teams deal with punctuation differently than you?
Team WaffleNugget (Md Abedin, Adam Abbas) dealt with punctuation by adding spaces before them in order for their madlibify to work.
Team Madify (Manjit Singh, Gavin Zheng) dealt with punctutation by deleting the punctuation and then adding them back in at the end.
3. Which approach do you prefer and why?
I prefer Team WaffleNugget's approach because adding in the punctuation at the end can be confusing,
while Team WaffleNugget just added a space before the punctuation and dealt with it through their madlibify by using indexes.
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

#print check('joke')
#print check('not')
        
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

story = """
Once upon a time, a <NOUN-SINGULAR> <VERB-PAST-SINGULAR> to <VERB> the way <NOUN-SINGULAR> <VERB-PAST-SINGULAR>.
<NOUN-SINGULAR> <VERB-PAST-SINGULAR> it would help him <VERB> more <ADVERB>.
<NOUN-SINGULAR> put on the skin of a <NOUN-SINGULAR>, then <NOUN-SINGULAR> <VERB-PAST-SINGULAR> with <NOUN-SINGULAR> into the <NOUN-SINGULAR>.
Even the <NOUN-SINGULAR> was <VERB-PAST-SINGULAR> by his <ADJECTIVE> <NOUN-SINGULAR>.
In the evening, the <NOUN-SINGULAR> <VERB-PAST-SINGULAR> him in with the rest of the <NOUN>.
<NOUN-SINGULAR> <VERB-PAST-SINGULAR> the <NOUN-SINGULAR> and made sure it was <ADJECTIVE> before he <VERB-PAST-SINGULAR> to <NOUN-SINGULAR>.
In the middle of the night, he <VERB-PAST-SINGULAR> back to the <NOUN-SINGULAR> to <VERB> some <NOUN> for the next day.
Instead of a <NOUN-SINGULAR>, though, he <VERB-PAST-SINGULAR> the <NOUN-SINGULAR>, killing <NOUN-SINGULAR> instantly.
Those who look to <VERB> others will be <VERB-PAST-SINGULAR> themselves.
"""
print madlibify(story)
