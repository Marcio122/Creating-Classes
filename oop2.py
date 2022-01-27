se1 = ['Software Engineer', 'Max', '20', 'Junior', 5000]
se2 = ['Software Engineer', 'Lisa', '25', 'Senior', 7000]


#class
class SoftwareEngineer:
    
    #class attributes
    alias = "Keyboard Magician"

    
    def __init__(self, name, age, level, salary):
       #instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    #instance method
    def code(self):
        print(f"{self.name} has a {self.level} position")
    
    
    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")


#instance
se1 = SoftwareEngineer('Max', '20', 'Junior', 5000)
print(se1.name, se1.age) 

print(SoftwareEngineer.alias)
se2 = SoftwareEngineer('Lisa', '25', 'Senior', 7000)
print(se2.name, se2.age)
print(SoftwareEngineer.alias)

se1.code()
se2.code()
se1.code_in_language("Python")