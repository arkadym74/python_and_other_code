try:
    answer = 12 / 0
    print(answer)
except:
    print("An error has occured")


try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1 / userInput2
    print("The answer is ", answer)
    myFile = open("missing.txt", 'r')
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Uknown error:", e)

except ValueError as e:
    print(e)
