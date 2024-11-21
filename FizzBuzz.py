#Writing a program that prints the numbers from 1 to 50. 
# For multiples of 3,it will  print "Fizz" instead of the number.
#  For multiples of 5, it will print "Buzz". 
# For numbers which are multiples of both 3 and 5, it will print "FizzBuzz"

for i in range (1 , 51):  
    if i % 3 == 0 and i % 5 == 0:
        print(" FizzBuzz ")
    elif i % 3 == 0:
        print( "Fizz" )
    elif i % 5 == 0:
        print( "Buzz" )
    else:
        print(i) 