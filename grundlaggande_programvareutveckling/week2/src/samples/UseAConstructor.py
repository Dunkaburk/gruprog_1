# package samples

#  * A constructor is a method called with same name as the class.
#  * but defined using the built-in name __init__
#  * It's used to initialize an objects instance variables with values from the
#  * parameters.
#  *
#  * Often there is a name clash between instance variables and parameters, prefix instance
#  * variables with 'this'

def use_constructor_program():
    dog = Dog()  # One way to initialize ...
    dog.name = "Fido"
    dog.age = 13  # Gaaaaaahhhhh, tiresome ...

    cat = Cat("Olle", 5)  # ... simpler to use a constructor
    print(cat.owner)  # owner set by constructor
    print(cat.age)  # color set by constructor


# ------- Classes ----------------------

class Dog:
    name: str = ""
    age: int = 0

    # # There is a no-args constructor here - implicit, invisible.
    # # It looks like this:
    # def __init__(self):
    #     pass


class Cat:
    owner: str = ""  # Instance variable
    age: int = 0

    # Add an own constructor (method). Two params!
    def __init__(self, owner, age):
        self.owner = owner  # 'self' used because of name clashes, owner/owner
        self.age = age
