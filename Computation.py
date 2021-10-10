print("S = 1 + 1/2 + 1/4 + 1/8 + ... + 2/2^n")


def AlgebraicForm(n):
    if n == 1: 
        return 1
    elif n == 0:
        return "The sum of the above sequence"
    else:    
        return 2/2**n + AlgebraicForm(n-1)


def DoIt():
    n = int(input("How many terms from this series do you wanna add?:"))
    for i in range(n):
        print(AlgebraicForm(i+1))
    DoIt()

DoIt()
