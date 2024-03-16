try: 
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divide by zero not allowed")
except ValueError as err: 
    print(err)
    print("Please only enter integer numbers")
except:
    print("Invalid status")