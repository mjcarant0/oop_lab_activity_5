class Animal: 
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
    
    def make_sound(self): # generic animal sound
        print("Makes a generic animal sound.")

    def describe(self): # describe the animal
        print(f"{self.__class__.__name__} - Name: {self.name}, Age: {self.age}")