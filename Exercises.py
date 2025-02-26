# Multiplicação de dois números naturais, através de somas sucessivas (Ex.: 6 ∗ 4 = 4 + 4 + 4 + 4 + 4 + 4).

def Recursive_Multiplication(n,m):
    if(m==0):
        return 0
    return n + Recursive_Multiplication(n,m-1)

# print(Recursive_Multiplication(6, 4))  
# print(Recursive_Multiplication(3, 5))  
# print(Recursive_Multiplication(7, 0)) 

# Soma de dois números naturais, através de incrementos sucessivos (Ex.: 3 + 2 = + + (+ + + 1)).

def Recursive_Sum(n1, n2):
    if n2 == 0:  
        return n1
    return Recursive_Sum(n1 + 1, n2 - 1) 


# print(Recursive_Sum(3, 2)) 
# print(Recursive_Sum(0, 7))  
# print(Recursive_Sum(10, 0)) 

# Cálculo de 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.

def Recursive_Sum_2(n,limit):
    if n > limit:
        return 0
    return 1/n + Recursive_Sum_2(n+1,limit)

# print(Recursive_Sum_2(1, 4))   
# print(Recursive_Sum_2(1, 10))  
# print(Recursive_Sum_2(1, 1))   

# Inversão de uma string.

def reverse_string(s):
    if len(s) == 0: 
        return s
    return reverse_string(s[1:]) + s[0]  

# print(reverse_string("augusto"))  
# print(reverse_string("carro"))  

# Gerador da sequência dada por:
# F(1) = 1
# F(2) = 2
# F(n) = 2 ∗ F(n − 1) + 3 ∗ F(n − 2).

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2 * F(n - 1) + 3 * F(n - 2)

print(F(1)) 
print(F(2))  
print(F(3)) 
print(F(4)) 
print(F(5))  


