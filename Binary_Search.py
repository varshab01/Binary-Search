List = [0,2,4,6,8,10,12]#6 is middle number
number = int(input("What is your number?"))
 
def our_binary_search(number, List):
    high = int(len(List) - 1)
    low  = 0
    middleNum = int(high + low)//2

    while (low < high):

        if(number == List[middleNum]):
            return True

        elif(number<List[middleNum]):
            high = int(middleNum - 1)
            middleNum = int(high + low)//2
            
        elif(number>List[middleNum]):
            low = int(middleNum + 1)
            middleNum = int(high + low)//2

    return False

if(our_binary_search(number, List)):
    print("Your number has been found")

else:
    print("Your number is not in the list")
    



        
