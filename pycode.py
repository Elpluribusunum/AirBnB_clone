#!/usr/bin/python3

class Person:
    def __init__(self, name, age):
        #Initialize the person object with a name and age.
        self.name = name
        self.age = age


    def introduce(self):
        """Introduce the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."



def main():
    """Main function"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    person = person(name, age)
    introduction = person.introduction()


    print(introduction)



if __name__ == "__main__"
    main()
