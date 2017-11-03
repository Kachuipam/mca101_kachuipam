#import pdb

def mergeList(list1,list2,list3=[],count1 = 0,count2 = 0):
    #pdb.set_trace()
    '''
    Objective: To merge two sorted list
    '''
    if (count1 == len(list1) and count2 == len(list2) ):
        return list3
        
    if (count1 == len(list1)):
        list3.append(list2[count2])
        count2 = count2+1
        return mergeList(list1,list2,list3,count1,count2)
    
    if (count2 == len(list2)):
        list3.append(list1[count1])
        count1 = count1+1
        return mergeList(list1,list2,list3,count1,count2)   
    
    if list1[count1] < list2[count2]:
        list3.append(list1[count1])
        count1=count1+1  
    else:
        list3.append(list2[count2])
        count2 = count2+1
        
    return mergeList(list1,list2,list3,count1,count2)
        
            
list1 = [32,54,76]
list2 = [23,59]
list3 = mergeList(list1,list2)
print(list3)
