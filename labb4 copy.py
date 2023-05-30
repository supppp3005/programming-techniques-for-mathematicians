# LABB 4



from labb2 import *

p = [2, 0, 1]
q = [-2, 1, 0, 0, 1]


#Uppgift 1

# 1.A

def symbolic_derivative(p_list):
    derivata = [p_list[i] * i for i in range(1, len(p_list))]
    return derivata

#print(symbolic_derivative(p)) 
#print(symbolic_derivative(q)) 
#print(symbolic_derivative([1]))
#print(symbolic_derivative([]))
#print(doly_to_string(symbolic_derivative(p)))
#print(doly_to_string(symbolic_derivative(q)))
#print(doly_to_string(symbolic_derivative([1])))
#print(doly_to_string(symbolic_derivative([])))



# 1.B

p_fun = lambda x: eval_poly(p,x)
q_fun = lambda x: eval_poly(q,x)



def numeric_derivative(f,h):
    return lambda x: (f(x+h)-f(x-h))/(2*h)  # själv funktionen av approximera derivatan

#print(numeric_derivative(p_fun,0.1)(0))
#print(numeric_derivative(p_fun,0.1)(1))
#print(numeric_derivative(p_fun,0.1)(2))
#print(numeric_derivative(q_fun,0.1)(2))
#print(numeric_derivative(q_fun,0.1)(-2)) 


#print(eval_poly(symbolic_derivative(p),0))
#print(eval_poly(symbolic_derivative(p),1))
#print(eval_poly(symbolic_derivative(p),2))
#print(eval_poly(symbolic_derivative(q),2))
#print(eval_poly(symbolic_derivative(q),-2))





#Uppgift 2

def print_poly_from_file(f):
    start = 0
    with open(f, 'r') as h:
        for row in h:
            start +=1
            word = row.split(' ')
            word = list(map(int, word))
            polynom = doly_to_string(word)
            print(polynom)
    
    


#print_poly_from_file('polynom.txt')


# Uppgift 3
    
import numpy as np


# 3.A

def mul_poly(p_list,q_list):
    a = np.array(p_list)      
    b = np.array(q_list)           # omvadla P-list,q_list till numpy array
    result = np.polymul(a,b)       
    n=result.tolist()
    return drop_zeroes(n)         # ta bort noll och retunera rsultat
    
#print(mul_poly([1,2,3],[2,3,4]))      
#print(mul_poly([],[2,3,4]))    
#print(mul_poly([1,2,3],[]))    
#print(mul_poly([1,2,3],[-2,4,3,-17]))    



# 3.B


def coeff_product(p_list,q_list):
    
    
    d= drop_zeroes(p_list) 
    f = drop_zeroes(q_list)
    a = np.array(d)    
    b = np.array(f)
    if p_list == [] and len(q_list) == 1:
       return 0
    if q_list == [] and len(p_list)== 1:  
       return 0
    else:
        if p_list == [] and len(q_list) > 1:
           raise ValueError("the polynomials must have the same degree")
        if q_list == [] and len(p_list) > 1:  
           raise ValueError("the polynomials must have the same degree")
  
    
   
    mul= np.multiply(a,b)
    e = mul.tolist()
        
    if len(p_list) == len(q_list):
        return sum(e)
    
    if len(p_list) != len(q_list):
        raise ValueError("the polynomials must have the same degree")
       
    
# print(coeff_product([1,2,3],[2,3,4]))
# print(coeff_product([1],[4]))
# print(coeff_product([1,2,3,0,0],[4,3,2,0]))
# print(coeff_product([],[0]))
# print(coeff_product([],[2]))
# print(coeff_product([3],[0]))
# print(coeff_product([1,0,1],[4,0]))
# print(coeff_product([4,0],[1,1]))






    
    
    
    
