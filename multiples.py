#Declare a variable to store sum
sum_of_multiples = 0

#loop through all the numbers from 1 to 1000 (exclusive)
for i in range(1,1000):
  if(i%3 == 0):
    sum_of_multiples = sum_of_multiples + i

print("Here is a sum of all multiples of 3:", sum_of_multiples)

#Function to calculate multiples of a number


def sumOfMultiples():
  sum_of_multiples = input(
      "Please enter a number to calculate the sum of multiples: ")
  result = 0

  '''A for loop with a range of numbers, goes through all integers as a 
  result of a digit entered at the beginning of a function. 
  Where numbers has no remainder resulting in a sum of all multiples'''

  sum_ = int(sum_of_multiples)
  for i in range(1, 1000):
    if(i % sum_ == 0):
      result = result + i
  print("This is a result of multiples of", sum_,
        ",and a sum of all multiples: ", result)


sumOfMultiples()
