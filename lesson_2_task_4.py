fizz_buzz_str = input ("Введите число: ")
fizz_buzz = int (fizz_buzz_str)

if (fizz_buzz % 3 == 0) and (fizz_buzz % 5 == 0):
         print("FizzBuzz")
else:
     if (fizz_buzz % 3 == 0):
      print("Fizz")
     else: 
        if (fizz_buzz % 5 == 0):
         print("Buzz")
  
      
print (fizz_buzz)