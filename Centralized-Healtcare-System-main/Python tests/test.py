def a():
    i = int(input())
    print(i,type(i))
    
def b():
    i = input()
    print(i,type(i))

while(True):
    choice = int(input("Enter the choice for input, 1 for string, 2 for integer, 3 to exit: "))
    if choice==1:
        b()
    elif choice==2:
        a()
    elif choice==3:
        break
    else:
        print("Incorrect choice of input")



