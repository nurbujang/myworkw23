# convoluted, to include 1 and 2
# results are too long 

def f(x):
    # If x is even, divide it by two
    if x % 2 == 0:
        return x // 2
    # if x is odd, multiply by 3, then add 1
    else:
        return (3 * x) + 1
    
def collatz(x):
    
    collatz_list = [] # numbers will be in a list

    if x == 1: # to include 1 in the list. If not, enter while loop
        collatz_list = [3*x+1]
        collatz_list.append(f(collatz_list[-1])) # append the last element of the sequence
        collatz_list.append(x)
        return collatz_list
    
    elif x == 2: # to include 2 in the list. If not, enter while loop
        return [x//2]
        
    while x != 1: # while loop
        x = f(x) 
        collatz_list.append(x) # list will append
    
    return collatz_list

# for verification of the first 10000 positive integers
for i in range(1, 10000+1):
    output = collatz(i)

# if verified, output will always end with 1
    if output[-1:] == [1]: # slicing and comparing
        print(i, "verified", output)