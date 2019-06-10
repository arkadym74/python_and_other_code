"""
Prime Numbers
"""

# Check if a number input by a user is prime or not.
# If it is not a prime number, print out that it's not a prime number.
# If it is a prime number, print out that it is a prime number.
# Hint: Prime numbers must be greater than 1.
# Hint: Don't worry about implementing a fancy algorithm - we'll say the number
# is smaller than 100.

# Challenge: For non-prime numbers, print an example of two factors.
# user_input = input("Enter a number to check if it's prime: ")

user_input = int(input("Enter a number to check if it's prime: "))

if user_input > 1:
   
   for num in range(2, user_input):
       if (user_input % num) == 0:
           print(user_input, "Is not a prime number")
           print(num,"times",user_input//num, "is", user_input)
           break
   else:
        print(user_input, "Is a prime number")
else:
    print(user_input,"Is not a prime number")
    

