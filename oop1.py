# position, name, age, level, salary
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

# Instance of this class
se1 = SoftwareEngineer('Max', '20', 'Junior', 5000)
print(se1.name, se1.age) 
# class attribute
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer('Lisa', '25', 'Senior', 7000)
print(se2.name, se2.age)
print(SoftwareEngineer.alias)

#recap
#classes are a blueprint
#create a instance(object)
#class vs instance
#instance attributes: defined in __init__(self)
#class attribute 