#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '08/06'

class dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sit")

    def roll_over(self):
        print(self.name.title() + " is roll")


class black_dog(dog):
    def __init__(self, name, age):
        super.__init__(self,name,age)
    pass
if __name__ == '__main__':
    my_dogs = dog("black",6)
    print(my_dogs.name.title())
    my_dogs.sit()
