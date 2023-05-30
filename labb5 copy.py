
#  Labb 5

from labb2 import *

import matplotlib.pyplot as plt

# Uppgift 1  En klass för polynom


class Polynomial:
    
     'En instansattribut som innehåller polynomet (representerad som en lista).'
    
     def __init__(self, p):
        self.p=drop_zeroes(p)    
        
     def degree(self):
         if self.p == []:
             return 0
         else:
           countgrad =len(self.p)-1
           return countgrad    
       
      

     def evaluate(self,x):
         'Return the value of function in x.'
         
         summa = eval_poly(self.p,x)
         return summa            






# Uppgift 2   En strängkonverterar
    
     def __str__(self):
         'Return the polynomial list in polynom.'
         return doly_to_string(self.p) 
     
        
     
        
     
 # Uppgift 4     # Uppgift 4 plotta grafen för polynom

     def plot_poly(self,filename,x_start=-10,x_end=10,color='b'):
         
         'Plot the function of given polynomial in grap and saves it in pdf file.'
               
         x = list(range(x_start,x_end +1))
         y = [eval_poly(self.p,x) for x in x]
         
         plt.plot(x,y,'b')
         plt.savefig(filename + '.pdf') 
                         
             

         
     
        
   # För uppgift 1  
        
p0 = Polynomial([0,1])
p1 = Polynomial([0,0,0,0,1,0])
p2 = Polynomial([0,0,4,5])
p3 = Polynomial([5,4,3,2,1])  
# print(p0.degree())
# print(p1.degree())
# print(p2.degree()) 
# print(p3.degree())
# print(p0.evaluate(7))
# print(p1.evaluate(1))
# print(p1.evaluate(2))
# print(p2.evaluate(0))
# print(p2.evaluate(1))
# print(p2.evaluate(2))
# print(p3.evaluate(1))

# print(Polynomial([]).degree())




  # för uppgit 2        
         
# print(str(p0))
# print(str(p1)) 
# print(str(p2))
# print(str(p3))


# För uppgift 4


p = Polynomial([3,-1,2,1])
p.plot_poly('myplot')






#  Uppgift 3  kvadratiska polynom genom arv

from math import sqrt as root

from cmath import sqrt as croot
 


class QuadraticPolynomial(Polynomial):
    
     def __init__(self,p):
         super().__init__(p) 
         
         if len(self.p) != 3:      # raise valueerror om grad är mer än 2
             raise ValueError("input is not a quadratic polynomial")
         
         
         
         
     def compute_roots(self):
         
         'Ränka ut nöllställen genom att använda pq-formeln'
         
         p_ = (self.p[1]) / (self.p[2]) # detta ger p till pqformeln
         q_ = (self.p[0]) / (self.p[2])  # detta ger q till pqformeln
         
         fall = (p_/2)**2-q_          
           # fall  sammanfattar tre olika fallen som kan förekomma i equationen.
             
                 
         if fall > 0:   # i detta fall har vi två rella nöllställen
             return [(-p_/2)+ root(fall), (-p_/2)- root(fall)]
        
         if fall == 0:    # i detta fall har vi ett reall nöllställe
             return [((-p_/2))]
         
            
         if fall < 0:        # i detta fall har vi komplexa nöllställen
             return [(-p_/2+ croot(fall)), (-p_/2 )- croot(fall)]
        
      
        # För uppgift 3
       
# qp1 = QuadraticPolynomial([1, 4, 4])
# qp2 = QuadraticPolynomial([2, 10, 1])
# qp3 = QuadraticPolynomial([2, 4, 8])
# print("The roots of",qp1,"are",qp1.compute_roots())
# print("The roots of",qp2,"are",qp2.compute_roots())
# print("The roots of",qp3,"are",qp3.compute_roots())
# qp4=QuadraticPolynomial([1, 4, 4, 4, 6])







































  