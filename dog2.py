class Dog:
   
    species = "Canis Familiaris"
   
    def __init__(self, name, age):
       
        self.name = name
        self.age = age
   
        # Instance Method

        def description(self):
            return f"{self.name} is {self.age} years old."

        #Another Instance Method
        def speak(self, sound):
            print(f"{self.name} says {sound}")
            
miles = Dog("Miles", 15)
miles.speak("Jesus Christ")
