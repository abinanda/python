# MODULE - 4 ASSIGNMENT KEY


### 1. Write a Python function to find the Max of three numbers.

n1 = int(input("Enter first number: "));
n2 = int(input("Enter second number: "));
n3 = int(input("Enter Third number: "));

def max_fun():
    if(n1 >= n2) and (n1 >= n3):
        l = n1
    elif(n2 >= n1) and (n2 >= n3):
         l = n2
    else:
         l = n3

    print("Largest number among  the three is", l)

max_fun()


### 2. Write a Python function to sum all the numbers in a list.

def sum_list(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
    return total


my_list = [1, 2, 3, 4, 5, 'hello']
total = sum_list(my_list)
print(total)


### 3. Write a Python function to multiply all the numbers in a list.

def multiply_list(numbers):
    product = 1
    for num in numbers:
        if isinstance(num, (int, float)):
            product *= num
    return product


my_list = [1, 2, 3, 4, 5, 'hello']
product = multiply_list(my_list)
print(product)


