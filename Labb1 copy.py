#Frågan 1

#def fahrenheit_to_celsius(t):
  #  t_celcius = t
   # return t_celcius

#svar = input('Ange en temperatur i Fahrenheit: ')
#t = fahrenheit_to_celsius(float(svar))
#print("Celsius: ", t)

#Svar 1
def fahrenheit_to_celsius(t):
   t_celcius = (t-32)*(5/9)
   return t_celcius

svar = float(input('Ange en temperatur i Fahrenheit: '))
t = fahrenheit_to_celsius(svar)
print("Celsius: ", t)

#Svar 2

def celsius_to_fahrenheit(p):
   t_fahrenheit = ((9/5)*p)+32
   return t_fahrenheit

svar = float(input('Ange en temperatur i Celsius: '))
p = celsius_to_fahrenheit(svar)
print("Fahrenheit: ", p)


#Svar3

svar = (input("Ange vilken temperaturskala du vill konvertera från, \
 celsius eller fahrenheit:"" "))
temp= float(input("ange temperatiur;"" "))

if   svar == "celsius": 
    
     p = celsius_to_fahrenheit(temp)
     print("Fahrenheit: ", p)
elif svar == "fahrenheit":
     t = fahrenheit_to_celsius(temp)
     print("Celsius: ", t)
     
     

