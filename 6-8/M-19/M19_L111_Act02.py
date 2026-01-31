for x in range(17): 
   if x % 20 == 0: 
      print("twist")

   elif x % 15 == 0:       
      pass # ignore or skip this code

   elif x % 5 == 0: 
      print("fizz")   

   elif x % 3 == 0:  
      print("buzz")    

   else: 
      print(x)
   
   print(f"test {x}") #still executed even though there's pass on x = 15
   print()