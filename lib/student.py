#!/usr/bin/env python

from user import User


class Student(User):
    def __init__(self, first_name, last_name, knowledge=[]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def learn(self, fact):
        if isinstance(fact, str):
            self.knowledge.append(fact)


# student_1 = Student("Ryan", "Block")
# print(student_1.first_name, student_1.last_name)
# student_1.learn("Hard work beat beats talent everyone day!")
# student_1.learn("Never give up! Ever!")

# print(student_1.knowledge)
