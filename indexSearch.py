def indexSearch(list1, pos = 0,index = 0):
    '''
    objective: To find the least element in an array and return its index.
    input paramenters:
        list1: The list to find the elements.
        elem: THe elements in the list.
        pos : Initialized to 0
    return value : The index of the least element
    approach : Use Recursion
    '''
    l=len(list1)
      
    if pos > l-1:
        return index
    
    if list1[pos] < list1[index]:
        index = pos
        pos += 1
        index=indexSearch(list1,pos,index)
        return index
    else :
        pos += 1
        index=indexSearch(list1,pos,index)
        return index
        
lst = [6,3,5,4,5]
least = indexSearch(lst)
print('The Elements is : ',lst)
print('The Index of the least element is = ',least)
