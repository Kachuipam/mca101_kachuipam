def insertList(list1,elements,pos = 1):
    '''
    objective: To insert an element in a list.
    input parameteres:
        elements: The elements in the list.
        pos: initialized to 0
        list1: List inputed by the user.
    Return Value : List, with the element inserted at required position.
    '''
    #approach: Use recursion
    
    if elements > list1[-1]:
        list1.append(elements)
        return
    elif elements > list1[pos] and element < [pos+1]:
        list.insert(pos+1,elements)
        pos = pos+1
        return
    else:
        pos = pos+1
        insertList(list1,elements,pos)

lst = [1,2,3,4,5,6,7]
elements = 8
insertList(lst,elements)
print('The New list = ',lst)
