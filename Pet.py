class Pet:
    def __init__(self, name, animal, age):
        self.__name = name
        self.__animal_type = animal
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def set_animal_type(self, animal):
        self.__animal = animal

    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age




def main():
    _name = input("Enter the name of your pet:")
    _animal = input("Enter the type of pet you have:")
    _age = float(input("Enter the age of you pet:"))

    my_pet = Pet(_name,_animal,_age)

    print("Your pet's name is", my_pet.get_name())
    print("Your pet's is a", my_pet.get_animal_type())
    print("Your pet's is", my_pet.get_age(), "years old")


main()
