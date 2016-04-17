#Henry Zheng
#IntroCS2 pd8
#HW18 -- 000 000 111 v.2
#2016-03-21

#1. bondify(name)

def bondify(name):
    n = 0
    while name[n] != " ":
        n -= 1                                                 #essentially goes backwards
    return name[n+1:] + str(", ") + name                       #returns "last_name, full_name"

print bondify("James Bond")                                    #should be "Bond, James Bond"

#2. replace(s,q,r)

def replace(s,q,r):
    if s.find(q) != -1:                                        #checks to make sure q can be found in the string
        return s[:s.find(q)] + r + s[s.find(q)+len(q):]        #returns everything before q, exclusive, replaces q with r, and then adds everything after the length of q, essentially adding the rest of s, after q
    else:                                                      #if q is not found in the string
        return s                                               #returns original string

print replace("Winter is coming", "Winter", "Spring")          #should be "Spring is coming"
print replace("Dolphins run this planet", "dolphins", "mice")  #should be "Dolphins run this planet"
