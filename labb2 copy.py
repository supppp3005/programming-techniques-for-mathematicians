# Labb 2


# Uppgift 1

p=[2,0,1]
q=[-2,1,0,0,1]


def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0

    # Collect a list of terms

    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff)) 
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        degree += 1

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string

#print(poly_to_string(p))
#print(poly_to_string(q))


#Uppgift 2

a=[]
b=[0,0,0]
def doly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0

    # Collect a list of terms
    
    if p_list == []:
        terms.append("0")# Retunerar 0 om listan är tom.
    if p_list.count(0) == len(p_list):
        return 0 # om litan består bara av 0 får vi 0.
    for coeff in p_list:
        if degree == 0 and coeff != 0:
            terms.append(str(coeff)) 
        elif degree == 1:
            if coeff == 1:
                terms.append('x')
            elif coeff != 0:
                terms.append(str(coeff)+'x')
        else:
            if coeff == 1:
                terms.append('x^' + str(degree))
            elif coeff !=0:  
                term = str(coeff) + 'x^' + str(degree)
                terms.append(term)
        degree += 1

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string
    

#print(doly_to_string(p))
#print(doly_to_string(q))
#print(doly_to_string(a))
#print(doly_to_string(b))



#uppgit 3

# Svar A

def drop_zeroes(p_list):
    
    while p_list and p_list[-1] == 0: # om det är nollor i slutet av listan
        p_list.pop()                  # detta tar bort nolla.
    return p_list

#print(drop_zeroes([1,2,0,0]))
#print(drop_zeroes([1,0,2]))
#print(drop_zeroes([0,0,0]))


# Svar B

def eq_poly(p_list,q_list):
     while p_list and p_list[-1] == 0:
        p_list.pop()
     while q_list and q_list[-1] == 0:
        q_list.pop()
        
     if p_list == q_list:    # testar om de två lisan är lika.
     
         return True
     else:
         return False

#print(eq_poly([1,2,3],[1,2,3,0]))
#print(eq_poly([1,2,3],[1,2,3]))
#print(eq_poly([1,0,2],[1,2,3]))    


#uppgift 4
def eval_poly(p_list,x):
    grad = 0
    summan = 0
    for coeff in p_list:
        summan += coeff*x**grad
        grad += 1
    return summan
        
#print(eval_poly(p,0))  
#print(eval_poly(p,1))  
#print(eval_poly(p,2))  
#print(eval_poly(q,2))  
#print(eval_poly(q,-2))       


    
#uppgift 5
# A Byt tecken på alla koeffieienter
def neg_poly(p_list):
    p_list_negation = []
    for coeff in p_list:
        p_list_negation.append((coeff)*(-1))
    return p_list_negation
#print(neg_poly(p))
  

#B Addera koefficienter
def add_poly(p_list, q_list):
    
    if len(p_list) > len(q_list):  # om p_list elngth ör större än q_list lenght
        a=p_list.copy()             
        b=q_list.copy()
    else:
        a=q_list.copy()
        b=p_list.copy()

    for i in range(len(b)):    
        a[i] += b[i]  # addera list från b i a.
    return a
        
#print(add_poly(p,q)) 


# C     subtratktioner
def sub_poly(p_list,q_list):
    sub = add_poly(p_list,neg_poly(q_list))
    return sub
#print(sub_poly(p,q)) 
        
#print(eq_poly(add_poly(p,q),add_poly(q,p)))
#print(eq_poly(sub_poly(p,p),[]))   
#print(eq_poly(sub_poly(p,neg_poly(q)),add_poly(p,q)))    
#print(eq_poly(add_poly(p,p),[]))   
#print(eq_poly(sub_poly(p,q),[4, -1, 1, 0, -1]))
#print(eval_poly(add_poly(p,q),12) == eval_poly(p,12) + eval_poly(q,12))
    
   
    
   
    

