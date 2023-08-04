# def factorial(n):
#     pr = 1
#     print(range(n))
#     for i in range(n, 1, -1):
#         pr = pr * i
#         print(i)
#     print(pr)
        
def factorial(n):
    if n<= 1:
        return 1
    else:
        return n * factorial(n - 1)
        
         
    
    
print(factorial(3))