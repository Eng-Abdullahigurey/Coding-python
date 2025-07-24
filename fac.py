#Functional factorial:
def factorial(n):
    result= 1
    for i in range(1, n + 1):
        result *=1
    return result
num=int(input("Enter a number to find factorial:"))
print("Factorial is " , factorial(num))