"""
Exception Handling
    ---> Error is the superclass. It is more of compile time issus
    ---> Exceptions are the logical errors which can be raised at the run-time.

"""

"""
try - except block
    ---> Statement which can be raise the exception are kept inside the try block
    ---> Statement which can handle the exception are kept inside the except block

1. ValueError 
2. NameError
3. ImportError
4. EOFError(EOF--> END OF FILE ERROR)
5. IOError(IO --> INPUT/OUTPUT ERROR)

"""

try:
    amount1 = int(input("Enter the amount 1 - "))
    daysWorked = int(input("Enter the days worked- "))
    Salary = amount1 / daysWorked
    print(Salary)

except ZeroDivisionError:
    print("You are dividing the number by zero! please try again. ")

except ValueError:
    print("You are dividing the integer with non-integer value. Please try again. ")


except:
    print("Something went wrong. ")

else:
    print("This is executed only if the try clause does not raise any exception. ")

finally:
    print("No matter, if an exception is raised or not. I will always and always execute. ")

print("This is the regular workflow of the code. ")

"""
THE CODE DOES NOT RAISE ANY EXCEPTION
ELSE BLOCK
"""