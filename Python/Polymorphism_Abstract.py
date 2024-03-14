""""
POLYMORPHISM
----> One name, multiple forms
----> Python does not support method overloading

Overloading
a. Method overloading
b. Constructor Overloading
c. Operator Overloading

2.  over-riding
a. Method Overriding
b.  Constructor Overloading



"""

# contrutor overloading
# Python does not support constructor overloading
# class Test1:
#   def __init__(self):
#       print(f"This is constructor 1")
#
#   def __int__(self, x):
#      self.x = x
#      print(f"This is value of x - {self.x} in Test 1")
#

# obj = Test1()
# obj2 = Test1(20)


"""
Operator Overloading

<Operand> <Operator><Operand>
10 + Ashish
Same type of operator will support
"""
print(10 + 10)
print("GHI" + "tIM")
print([1, 2, 3] + [3, 5, 6])
print("Tom" * 4)


class Operator:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        totalMarks = self.marks + other.marks
        return totalMarks

    def __sub__(self, other):
        totalMarks = self.marks - other.marks
        return totalMarks


a = Operator(60)
b = Operator(30)

print(a + b)
print(a - b)

"""
Abstract Classes
--> There some set of instructions and that should follow
    --> We cannot directly create objects of the abstract class if the class contains abstract methods
Abstract Methods
    --> These methods do not have any implementation
    



"""

from abc import ABC
from abc import abstractmethod


class Exams(ABC):
    @abstractmethod
    def question1(self):
        """
        THIS QUESTION HAS TO BE ANSWERD IN 200 WORDS
        :return:
        """
        pass
    @abstractmethod
    def question2(self):
        """
        THIS QUESTION SHOULD BE OF 10 MARKS
        :return:
        """

        pass

    def question3(self):
        print("This is an optional case")


# cbse = Exams()
# cbse.question3()


class Smita(Exams):
    def question1(self):
        print("This is smita question 1")
    def question2(self):
        print("This is smita question 2")
    def question4(self):
        print("This is question 4")

smitaQuestion = Smita()
smitaQuestion.question4()
smitaQuestion.question2()
smitaQuestion.question1()
smitaQuestion.question3()
