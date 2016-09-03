def mode(L):
    ind = 1  #starts off at index 1 because we will start newL off at index 0
    newL = [0, L.count(L[0])]  #newL = [index, # of terms in L]
    newL2 = []  #if there is more than 1 mode
    while ind < len(L):
        count = L.count(L[ind])  #sets count as the # of terms in L
        if count > newL[1]:  #if count beats reigning champ
            newL = [ind, count]  #updates newL to new reigning champ
        if count == newL[1]:  #if count equals reigning champ
            newL2 += [L[ind]]  #adds this number to newL2
        ind += 1  #contines on the list
    if newL[1] == 1:
        return "no mode"  #if all numbers occur equally
    else:
        ans = [L[newL[0]]] + newL2  #combines all of the modes
        unique = []  #sets up unique list
        
        #to get unique terms
        for x in ans:
            if not x in unique:
                unique.append(x)
                
        if len(unique) == 1:
            return unique[0]  #if there is only one unique term
        else:
            ans = ""
            while len(unique) > 0:
                ans += str(unique[0]) + " "
                unique = unique[1:]  #continues on the list
            ans = ans[:-1]  #deletes last space
            return ans.replace(" ", ", ")  #replaces space with comma and space

print mode([1,2,3])  #should be "no mode"
print mode([1,2,2])  #should be 2
print mode([1,1,2,2])  #should be 1, 2
print mode([1,2,3,1,2,3])  #should be 1, 2, 3