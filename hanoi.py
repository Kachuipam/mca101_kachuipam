def towerOfHanoi(n,source,spare,target):
    '''
    objective: To Solve the problem of tower of hanoi.
    input parameters:
        n: Number of Disk
        source: The source 
    '''
    if n == 1:
        print('Move disk from ',source,'to',target)

    else:
        towerOfHanoi(n-1,source,target,spare)
        print('Move disk from ',source,'to',target)
        towerOfHanoi(n-1,spare,source,target)

def main():
    '''
    '''
    n = int(input('Enter the number of disk: '))
    towerOfHanoi(n,source,spare,target)

if __name__=='__main__':
    main()
