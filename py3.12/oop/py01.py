class Employee:
    # public variable
    company = 'Google'
    def __init__(self, name, salary):
        # private variables
        self.name = name
        self.__salary = salary
