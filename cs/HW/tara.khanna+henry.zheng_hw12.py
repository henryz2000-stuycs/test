# Dolphin Commando Squad: Tara Khanna and Henry Zheng
# IntroCS2 pd8
# HW12 -- PassJudgement
# 2016-03-10

# 1. pythTriple(a,b,c)
def pythTriple(a,b,c):
    if a==0 or b==0 or c==0:   #not a triangle
        return False
    elif a**2 + b**2 == c**2:  #assuming a and b are the smallest sides
        return True
    elif b**2 + c**2 == a**2:  #assuming b and c are the smallest sides
        return True
    elif a**2 + c**2 == b**2:  #assuming a and c are the smallest sides
        return True
    else:                      #not a right triangle
        return False

    
print pythTriple(0,0,0)      #should be False
print pythTriple(3,4,5)      #should be True
print pythTriple(3,4,6)      #should be False
print pythTriple(32,255,257) #should be True

# 2. gradeConv(g)
def gradeConv(g):
    if g>100:
        return "error_TOOSMART"  #over 100. AKA stuy level
    elif g>=90 and g<=100: 
        return "A"               #90-100
    elif g>=80:
        return "B"               #80-89
    elif g>=70:
        return "C"               #70-79
    elif g>=65:
        return "D"               #65-69
    else:
        return "F"               #less than 65

print gradeConv(110)  #should be error_TOOSMART
print gradeConv(100)  #should be A
print gradeConv(95)   #should be A
print gradeConv(80)   #should be B
print gradeConv(72)   #should be C
print gradeConv(68)   #should be D
print gradeConv(42)   #should be F

# 3. passJudgement(letterGrade)
def passJudgement(letterGrade):
    if letterGrade == "error_TOOSMART":
        return "Good Job :)"
    elif letterGrade == "A":
        return "A--Average :|"
    elif letterGrade == "B":
        return "B--Below Average"
    elif letterGrade == "C":
        return "C--Can't Eat Dinner :/"
    elif letterGrade == "D":
        return "D--Don't Come Home :("
    else:
        return "F--Find a New Family :'("
    
print passJudgement("error_TOOSMART")   #should be "Good Job :)"
print passJudgement("A")                #should be "A--Average :|"
print passJudgement("B")                #should be "B--Below Average"
print passJudgement("C")                #should be "C--Can't Eat Dinner :/"
print passJudgement("D")                #should be "D--Don't Come Home :("
print passJudgement("F")                #should be "F--Find a New Family :'("
