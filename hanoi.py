def towerOfHanoi(n,source,spare,target):
    '''
    objective: To Solve the problem of tower of hanoi.
    input parameters:
        n: Number of Disk
        source: The source
        spare : The spare pole
        target : The target pole
    Output : The required disk movement.
    '''
    
    if n == 1:
        print('Move disk from ',source,'to',target)
    elif n==0:
        return
    else:
        towerOfHanoi(n-1,source,target,spare)
        print('Move disk from ',source,'to',target)
        towerOfHanoi(n-1,spare,source,target)

def main():
    '''
    Objective : To generate the movements required to solve Tower of Hanoi
    User Inputs : 
        n: Number of Disk
        source: The source
        spare : The spare pole
        target : The target pole
    Output : The required disk movement.
    '''

    n = int(input('Enter the number of Disks: '))
    source = int(input('Enter the Source pole: '))
    spare = int(input('Enter Spare pole: '))
    target = int(input('Enter the Target pole: '))

    towerOfHanoi(n,source,spare,target)

if __name__=='__main__':
    main()
