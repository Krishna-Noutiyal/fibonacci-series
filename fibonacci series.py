# Creating a program that generates fibonacci series till the value you want

# fibonacci series
# 0,1,1,2,3,5,8,13,21 ...

import time

def wait(n=1):
    time.sleep(n)


wait()
try:
    Option = int(input(
    "\n\nWhat you want to do \n\n\t1) Print fibonacci series till 'n' terms\n\n\t2) Get the value of nth term\n\n[ Press 1 or 2 ] : "))
        
    if Option == 1:
        wait()

        User_Input = int(
            input("\nEnter the number till you want to print the Series : "))

        No1 = 0
        No2 = 1
        lst = [0,1]
        for i in range(2, User_Input):
            No3 = No1 + No2
            # print(No3)
            lst.append(No3)
            No1 = No2
            No2 = No3
            
        wait(2)

        print(f"\nThe fibonacci series till {User_Input}th term is : ", end=" ")
        
        wait(0.5)

        for items in lst:
            print(items, end=", ")
        
        wait()
        print("\n\n")

    elif Option == 2:
        wait()
        User_Input = int(
            input("\nEnter the nth term you want the value for : "))

        No1 = 0
        No2 = 1
        wait()
        print(No1)
        wait()
        print(No2)
        value = None
        for i in range(2, User_Input):
            No3 = No1 + No2
            # print(No3)
            value = No3
            No1 = No2
            No2 = No3
        
        wait()
        print(f"\n\nThe value of {User_Input}th term is : {value}", end="\n\n")

    else:
        wait()
        print("\n\tYou did something wrong please try again", end="\n\n")
except:
    wait()
    print("\n\n\tHmm, This shouldn't have happend ", end=" ")
    wait()
    print("\n\tSee if you did something wrong", end="\n\n")



'''
User_Input = int(input("Enter the number till you want to print the Series : "))

No1 = 0
No2 = 1
print(No1)
print(No2)
lst = [0,1]
for i in range(2,User_Input):
    No3 = No1 + No2
    # print(No3)
    lst.append(No3)
    No1 = No2
    No2 = No3
    # print(i)
    # print(f"No1 : {No1} and No2 : {No2}")


# print(lst)

'''
