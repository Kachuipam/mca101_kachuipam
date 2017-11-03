def calcPercentage(obMarks,mxMarks):
    '''
    objective : To calculate the percentage from the marks entered.
    input parameters : 
        obmarks : Marks obtained.
        mxmarks : Maximum Marks.
    appraoch : Divide the marks obtained by the maximum marks and then 
    multiply by 100. The result is the percentage.
    
    return : The value of percentage
    '''
    
    percent = (obMarks/mxMarks)*100
    return percent

def main():
    '''
    objective : To calculate the percentage from the marks entered.
    input parameters : 
        obmarks : Marks obtained.
        mxmarks : Maximum Marks.
    appraoch : Use the calcPercentage function
    '''
    obMarks = int(input('Enter marks secured : '))
    mxMarks = int(input('Enter total marks : '))
    print('The percentage scored is ',calcPercentage(obMarks,mxMarks),'%')
    
if __name__=='__main__':
    main()
