# package samples

# Using methods with parameters or return types of list of class objects.
def object_list_method_program():
    # Use own type Dog to create an array of dogs
    dogs = get_dogs()  # Call method to create and set data for all dogs

    for dog in dogs:
        print(f"Dog {dog.name} is {dog.age} years old")

    oldest = find_oldest(dogs)
    print("Oldest is " + oldest.name)


# This class captures the concept of a dog
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Method returning an array of dog objects
def get_dogs():
    n_dogs = int(input("How many dogs? > "))
    dogs = []
    for i in range(n_dogs):
        name = input(f"What's the name of dog {i+1}? > ")  # Fill in data
        age = input("How old is it? > ")
        dogs.append(Dog(name, age))
    return dogs


# Find oldest dog in array of dogs
# List of objects as parameter, returning single object
def find_oldest(dogs) -> Dog:
    index = 0
    max_age = dogs[index].age  # Assume first is oldest ...
    for i in range(len(dogs)):
        if dogs[i].age > max_age:
            index = i
            max_age = dogs[i].age
    return dogs[index]


if __name__ == "__main__":
    object_list_method_program()
