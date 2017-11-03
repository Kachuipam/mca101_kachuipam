import sys
sys.path.append('/home/administrator/Desktop/mca101/')
import areaSq
def main():
    '''
    objective: To find the area of Rectangle and square.
    user inputs:
         lenghth: Length of the rectangle
         breadth: Breadth of the rectangle
         side: Side of the square
    approach: Use return value for area of rectangle or area of square as per user.
    '''
    print('Press 1 to find the area of the rectangle: ')
    print('Print 2 to find the area of the square: ')
    choice = int(input('Enter Choice: '))
    if choice == 1:
        length = int(input('Enter the length of the rectangle: '))
        breadth = int(input('Enter the breadth of the rectangle:' ))
        print('Area of the rectangle = ',areaSq.areaRect(length,breadth))

    elif choice == 2:
        side = int(input('Enter the side: '))
        print('Area of the Square = ',areaSq.areaSquare(side))
    else :
        print('Wrong Input!!!\nExiting!!!')

if __name__=='__main__':
        main()
